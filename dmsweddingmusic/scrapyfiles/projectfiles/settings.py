#LOG_ENABLED=False

NEWSPIDER_MODULE = "projectfiles.spiders"
SPIDER_MODULES = "projectfiles.spiders"

EXTENSIONS = {
   'scrapy.telnet.TelnetConsole': None
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0
AUTOTHROTTLE_MAX_DELAY = 15
CONCURRENT_REQUESTS = 2

DOWNLOAD_MAXSIZE = 0
DOWNLOAD_WARNSIZE = 0

ROBOTSTXT_OBEY = False
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"

