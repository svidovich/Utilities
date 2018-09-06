from scrapy import Spider
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class listerSpider(Spider):
	name = "lister"
	ls = os.listdir(".")
	pwd = os.getcwd()

	def start_requests(self):
		url = sys.argv[1]
		yield Request(url=url, callback=self.parse_playlist)
	def parse_playlist(self, response):



#current = os.path.join(self.pwd, title)
#moved = os.path.join(self.pwd, 'archives', title)
#os.rename(current, moved)
