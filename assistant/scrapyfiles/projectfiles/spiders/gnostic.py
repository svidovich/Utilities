from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re


class gnosisSpider(Spider):
    name = "gnosis"
    # yapf: disable
    custom_settings = {
        # This is important! It allows us to use the download links from the pages to get files!
        'MEDIA_ALLOW_REDIRECTS': 'True',
        }
    # yapf: enable
    allowed_domains = ["gnosis.org"]
    def start_requests(self):
        url = "http://www.gnosis.org/library.html"
        yield Request(url=url, callback=self.parse_library)

    def parse_library(self, response):
	html = response.xpath('/html/body/table/tr/td[1]').extract()[0]
	for href, stack in re.findall('href="(.*?)><font face="Arial">(.*?)</font>"', html):
		print("href:{}\nstack:{}\n".format(href,stack))
