#LOG_ENABLED=False

NEWSPIDER_MODULE = "projectfiles.spiders"
SPIDER_MODULES = "projectfiles.spiders"

EXTENSIONS = {
   'scrapy.telnet.TelnetConsole': None
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 8
AUTOTHROTTLE_MAX_DELAY = 30
CONCURRENT_REQUESTS = 1

DOWNLOAD_MAXSIZE = 0
DOWNLOAD_WARNSIZE = 0

ROBOTSTXT_OBEY = False
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) "

