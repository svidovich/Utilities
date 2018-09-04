from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# This is a scraper which will get the current price of a grand exchange item
# This will likely be changed in the future

class naghammadiSpider(Spider):
    name = "gecp"
    # yapf: disable
    custom_settings = {
        # This is important! It allows us to use the download links from the pages to get files!
        'MEDIA_ALLOW_REDIRECTS': 'True',
        }
    # yapf: enable
    allowed_domains = ["runescape.com"]
    def start_requests(self, url=None):
	# Currently using an actual URL for testing purposes
        url = ""
        yield Request(url=url, callback=self.search_library)

