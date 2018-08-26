
# This spider roams the classics section of the gnosis.org website and collects all of the documents.


from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class classicsSpider(Spider):
    name = "classics"
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
        url = "http://www.gnosis.org/library/gs.htm"
        yield Request(url=url, callback=self.search_library)

    def search_library(self, response):
	html = response.xpath('/html/body/table/tr/td[2]/blockquote').extract()[0]
	for href, title in re.findall('<strong><a href="(.*?)">(.*?)</a>', html, re.DOTALL):
		url = "http://www.gnosis.org/library/{}".format(href)
		yield Request(url=url, meta={'title':title}, callback=self.collect_fragments)

    def collect_fragments(self, response):
	text = ''
	for node in response.xpath('//p'):
		text += node.xpath('string()').extract()[0]
	title = response.meta["title"] + ".gno"
	with open(title, "w") as file:
		file.write(text)
	current = os.path.join(self.pwd, title)
	moved = os.path.join(self.pwd, 'archives', title)
	os.rename(current, moved)
