 # -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os

class alchemySpider(Spider):
    name = "alchemy"
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
#    allowed_domains = ["gnosis.org"]
    def start_requests(self):
        url = "http://www.gnosis.org/library/alch.htm"
        yield Request(url=url, callback=self.search_library)

    def search_library(self, response):
	html = response.xpath('//li/a').extract()
	for link in html:
		href = re.findall('href="(.*?)">', link)[0]
		description = re.findall('>(.*?)</a>', link, re.DOTALL)[0]
		yield Request(url=href, meta={'title':description}, callback=self.parse_text)

    def parse_text(self, response):
	text = ''
	for node in response.xpath('//p'):
		text += node.xpath('string()').extract()[0]
	title = "Alchemy- " + response.meta["title"] + ".gno"
	with open(title, "w") as file:
		file.write(text)
	current = os.path.join(self.pwd, title)
	moved = os.path.join(self.pwd, 'archives', title)
	os.rename(current, moved)
