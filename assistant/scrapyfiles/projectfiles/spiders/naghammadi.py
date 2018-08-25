from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re


class naghammadiSpider(Spider):
    name = "naghammadi"
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
	html = response.xpath('/html/body/table/tr/td[2]/blockquote/ul/ul').extract()[0]
	for href, title in re.findall('href="(.*?)"><strong>(.*?)</strong>', html):
		if '/' in href:
			url = "http://www.gnosis.org{}".format(href)
		else:
			url = "http://www.gnosis.org/{}".format(href)
		yield Request(url=url, callback=self.search_library, meta={'title':title})
    def search_book(self, response):
	pass
