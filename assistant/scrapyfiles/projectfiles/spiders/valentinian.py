from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class valentinianLibrarySpider(Spider):
    name = "valentinian"
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
        url = "http://www.gnosis.org/library/valentinus/Valentinian_Writings.htm"
        yield Request(url=url, callback=self.collect_links)

    def collect_links(self, response):
	for node in response.xpath('//ol//a').extract():
		for href, title in re.findall('href="(.*)" target="_blank">(.*)</a>', node):
			title = title.replace("<i>", "").replace("</i>", "")
			if "../../" in href:
				href = href.split("../")[-1]
				url = "http://www.gnosis.org/{}".format(href)
			elif "../" in href:
				href = href.split("/")[-1]
				url = "http://www.gnosis.org/library/{}".format(href)
			yield Request(url=url, meta={'title':title}, callback=self.collect_writing)

    def collect_writing(self, response):
	text = ''
	for node in response.xpath('//p'):
		text += node.xpath('string()').extract()[0]
	title = "valentinian-teachings " + response.meta["title"] + ".gno"
	with open(title, "w") as file:
		file.write(text)
	current = os.path.join(self.pwd, title)
	moved = os.path.join(self.pwd, 'archives', title)
	os.rename(current, moved)


