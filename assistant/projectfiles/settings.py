BOT_NAME = "firmware"

#LOG_ENABLED=False

NEWSPIDER_MODULE = "projectfiles.spiders"

# Add the custom FTP crawler handler
DOWNLOAD_HANDLERS = {'ftp': 'firmware.ftp_utilities.FtpListingHandler'}

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
USER_AGENT = ""

