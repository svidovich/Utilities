from scrapy import Spider
from scrapy_splash import SplashRequest
from scrapy.http import Request, FormRequest, HtmlResponse
import urlparse
import re
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class listerSpider(Spider):
	name = "titlegrab"
	ls = os.listdir(".")
	pwd = os.getcwd()

	script = """
	function main(splash)
		local url = splash.args.url
		assert(splash:go(url))
		assert(splash:wait(2))
		return{
			html = splash:html()
		}
	end
	"""

	dlmwdict = {'scrapy_splash.SplashCookiesMiddleware':723, 'scrapy_splash.SplashMiddleware':725, 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810}
	smwdict = {'scrapy_splash.SplashDeduplicateArgsMiddleware':100}


	custom_settings = {
		# This is important! It allows us to use the download links from the pages to get files!
		'MEDIA_ALLOW_REDIRECTS': 'True',
		# This points to the location of the splash host.
		'SPLASH_URL': 'http://localhost:8050',
		'SPIDER_MIDDLEWARES': smwdict,
		'DOWNLOADER_MIDDLEWARES': dlmwdict,
		'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter'
	}

	def start_requests(self):
		print('begin')
#		filename = ""
#		with open(filename, "w+") as file:
#			json.dump(playlistdictionaries, file)
