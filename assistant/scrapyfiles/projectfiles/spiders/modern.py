 # -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os

class modernSpider(Spider):
    name = "modern"
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
        url = "http://www.gnosis.org/library/modern.htm"
        yield Request(url=url, callback=self.search_library)

    def search_library(self, response):
	html = response.xpath('//ul//a').extract()
	for link in html:
		href = re.findall('href="(.*?)">', link)[0]
		description = re.findall('>(.*)</a>', link)[0]
		if '..' in href:
			pass
		elif '/library/' in href:
			url = 'http://www.gnosis.org{}'.format(href)
		else:
			url = 'http://www.gnosis.org/library/{}'.format(href)
		try:
			yield Request(url=url, meta={'title':description}, callback=self.parse_text)
		except:
			print('Skipped URL.')

    def parse_text(self, response):
	text = ''
	for node in response.xpath('//p'):
		text += node.xpath('string()').extract()[0]
	title = "Modern- " + response.meta["title"] + ".gno"
	with open(title, "w") as file:
		file.write(text)
	current = os.path.join(self.pwd, title)
	moved = os.path.join(self.pwd, 'archives', title)
	os.rename(current, moved)
