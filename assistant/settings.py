BOT_NAME = "firmware"

#LOG_ENABLED=False

SPIDER_MODULES = ["firmware.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"

ITEM_PIPELINES = {
    "firmware.pipelines.FirmwarePipeline": 1,
}

# Add the custom FTP crawler handler
DOWNLOAD_HANDLERS = {'ftp': 'firmware.ftp_utilities.FtpListingHandler'}


# Add Downloader Middlewares for Splash headless
# DOWNLOADER_MIDDLEWARES = {
#         'scrapy_splash.SplashCookiesMiddleware':723,
#         'scrapy_splash.SplashMiddleware':725,
#         'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
#         }
# Add Spider Middlewares for Splash Headless
# SPIDER_MIDDLEWARES = {
#         'scrapy_splash.SplashDeduplicateArgsMiddleware':100
#         }
# Add URL Endpoint. Make sure the container is running and has the correct port
# SPLASH_URL = 'http://localhost:8050'
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


EXTENSIONS = {
   'scrapy.telnet.TelnetConsole': None
}
FILES_STORE = "./output/"

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0
AUTOTHROTTLE_MAX_DELAY = 15
CONCURRENT_REQUESTS = 8

DOWNLOAD_TIMEOUT = 1200
DOWNLOAD_MAXSIZE = 0
DOWNLOAD_WARNSIZE = 0

ROBOTSTXT_OBEY = False
USER_AGENT = "FirmwareBot/1.0 (+https://github.com/firmadyne/scraper)"

# Changes what's allowed as a download url in pipelines.py
ATYPICAL_DOWNLOAD_EXTENTIONS_ENABLED = False
# SQL_SERVER = "127.0.0.1"
