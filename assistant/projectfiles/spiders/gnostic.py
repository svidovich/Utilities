from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re


# This spider serves as a study for the use of posting to submit forms using scrapy without
# using a headless browser. For this reason, this scraper will be especially documentation-heavy.

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
        url = "http://www.gnosis.org/library/alch.htm"
        yield Request(url=url, callback=self.parse_library)

    def parse_library(self, response):
	html = response.xpath('/html/body').extract()[0]
	print(html)
