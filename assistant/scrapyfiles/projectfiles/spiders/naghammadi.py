from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os


class naghammadiSpider(Spider):
    name = "naghammadi"

    ls = os.listdir(".")
    pwd = os.getcwd()
    if 'archives' not in ls:
	os.mkdir("archives")

    # yapf: disable
    custom_settings = {
        # This is important! It allows us to use the download links from the pages to get files!
        'MEDIA_ALLOW_REDIRECTS': 'True',
        }
    # yapf: enable
    allowed_domains = ["gnosis.org"]
    def start_requests(self):
        url = "http://www.gnosis.org/naghamm/nhlalpha.html"
        yield Request(url=url, callback=self.search_library)

    def search_library(self, response):
	html = response.xpath('/html/body').extract()[0]
	for href, title in re.findall('href="(.*?)"><strong>(.*?)</strong>', html):
		if '/' in href:
			url = "http://www.gnosis.org{}".format(href)
		else:
			url = "http://www.gnosis.org/naghamm/{}".format(href)
		yield Request(url=url, callback=self.search_book, meta={'title':title})
    def search_book(self, response):
	text = ''
	for node in response.xpath('//p'):
		text += node.xpath('string()').extract()[0]
	title = response.meta["title"] + ".gno"
	with open(title, "w") as file:
		file.write(text)
