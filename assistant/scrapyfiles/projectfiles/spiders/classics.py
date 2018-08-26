
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

#	current = os.path.join(self.pwd, title)
#	moved = os.path.join(self.pwd, 'archives', title)
#	os.rename(current, moved)
