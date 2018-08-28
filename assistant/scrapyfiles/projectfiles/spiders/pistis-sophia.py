from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class pistisSophiaSpider(Spider):
    name = "pistissophia"
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
        url = "http://www.gnosis.org/library/pistis-sophia/index.htm"
        yield Request(url=url, callback=self.search_library)

    def search_library(self, response):
	html = response.xpath('/html/body/table/tr/td[2]/blockquote[2]').extract()[0]
	for href, chapter in re.findall('href="(.*?)">(.*?)</a>', html, re.DOTALL):
		if "Chapter" in chapter:
			url = "http://www.gnosis.org/library/pistis-sophia/{}".format(href)
			yield Request(url=url, meta={'chapter':chapter}, callback=self.collect_chapter)

    def collect_chapter(self, response):
	text = ''
	for node in response.xpath('//p'):
		text += node.xpath('string()').extract()[0]
	title = "pistis-sophia " + response.meta["chapter"] + ".gno"
	with open(title, "w") as file:
		file.write(text)
	current = os.path.join(self.pwd, title)
	moved = os.path.join(self.pwd, 'archives', title)
	os.rename(current, moved)
