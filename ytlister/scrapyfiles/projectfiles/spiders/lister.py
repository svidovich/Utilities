from scrapy import Spider
from scrapy_splash import SplashRequest
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

	script = """
	function main(splash)
		local url = splash.args.url
		assert(splash:go(url))
		assert(splash:wait(1))
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
		url = 'https://www.youtube.com/playlist?list=FLQaroSiSNdFLMlPgpB6Ah7Q'
		yield SplashRequest(url=url, 
					callback=self.parse_playlist,
					endpoint='execute',
					args={
						'lua_source':self.script
					})
	def parse_playlist(self, response):
		html = response.xpath('//*[@id="contents"]').extract()[0]
		print(html)


#current = os.path.join(self.pwd, title)
#moved = os.path.join(self.pwd, 'archives', title)
#os.rename(current, moved)
