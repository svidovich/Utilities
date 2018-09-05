from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class grsmeadSpider(Spider):
    name = "grsmead"
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
        url = "http://www.gnosis.org/library/grs-mead/mead_index.htm"
        yield Request(url=url, callback=self.search_library)

    def search_library(self, response):
	html = response.xpath('/html/body').extract()[0]
	for href, title in re.findall('<b><a href="(.*?)">(.*?)</a></b>', html, re.DOTALL):
		print("{} {}".format(href, title))
