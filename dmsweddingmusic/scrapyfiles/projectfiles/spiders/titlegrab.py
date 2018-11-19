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
	data = ''
	filename = 'output'
	with open(filename, 'r') as file:
		data = json.load(file)


	# Youtube uses a whole fuckload of JS, so let's
	# use splash to go about this

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
		for song in self.data:
			queryurl = 'https://www.youtube.com/results?search_query={}+{}'.format(song['artist'], song['title']).replace(' ','+')
			yield SplashRequest(url=queryurl,
						callback=self.parsepage,
						endpoint='execute',
						args={
							'lua_source':self.script
						})

	def parsepage(self, response):
		link = response.xpath('//a[@id="video-title"]').extract_first()
		print(link)




#		filename = ""
#		with open(filename, "w+") as file:
#			json.dump(playlistdictionaries, file)
