from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
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

	# This allows me to write a function that gets called when the spider closes
	def __init__(self):
		dispatcher.connect(self.spider_closed, signals.spider_closed)


	name = "titlegrab"
	data = ''
	filename = 'output'
	with open(filename, 'r') as file:
		data = json.load(file)

	songlist = []
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
		'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
		'COOKIES_ENABLED': 'False'
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
		link = response.xpath('//a[@id="video-title" and @aria-label]').extract()[1]
		href = re.findall('title="(.*)" href="(.*)"', link)
		song = {}
		songdata = href[0]
		song['title'] = songdata[0]
		song['link'] = songdata[1]
		print(song)
		self.songlist.append(song)


	def spider_closed(self, spider):

		filename = "masterlist"
		with open(filename, "w") as file:
			json.dump(self.songlist, file)
