#coding:utf-8
from scrapy import Spider
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.http import Request, FormRequest, HtmlResponse
from w3lib.html import remove_tags
import urlparse
import re
import sys
import pprint
import time
class wikicategoryscraperSpider(Spider):
    name = "categories"
    custom_settings = {
        # This is important! It allows us to use the download links from the pages to get files!
        'MEDIA_ALLOW_REDIRECTS': 'True',
        'FEED_URI_OVERWRITE': 'False'
        }
    allowed_domains = ["wikipedia.org"]
    phones = []
    missed = []
    s = 0
    f = 0
    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)
    def start_requests(self):
        urls = ["https://en.wikipedia.org/w/index.php?title=Category:Samsung_mobile_phones&pageuntil=Samsung+Galaxy+On8#mw-pages",
                "https://en.wikipedia.org/w/index.php?title=Category:Samsung_mobile_phones&pagefrom=Samsung+Galaxy+On8#mw-pages",
                "https://en.wikipedia.org/w/index.php?title=Category:Smartphones&pageuntil=List+of+smartphones+with+HD+Voice+support#mw-pages",
                "https://en.wikipedia.org/w/index.php?title=Category:Smartphones&pagefrom=List+of+smartphones+with+HD+Voice+support#mw-pages",
                "https://en.wikipedia.org/w/index.php?title=Category:Smartphones&pagefrom=Palm+Centro#mw-pages",
                "https://en.wikipedia.org/w/index.php?title=Category:Smartphones&pagefrom=Sony+Xperia+Z3%2B#mw-pages",
                "https://en.wikipedia.org/wiki/Category:Android_(operating_system)_devices",
                "https://en.wikipedia.org/w/index.php?title=Category:Android_(operating_system)_devices&pagefrom=HTC+U+series#mw-pages",
                "https://en.wikipedia.org/w/index.php?title=Category:Android_(operating_system)_devices&pagefrom=Nexus+5#mw-pages",
                "https://en.wikipedia.org/w/index.php?title=Category:Android_(operating_system)_devices&pagefrom=Samsung+Galaxy+Tab+S2+9.7#mw-pages",
                "https://en.wikipedia.org/wiki/Category:Mobile_phones_introduced_in_2018",
                "https://en.wikipedia.org/wiki/Category:IPhone"]
        for url in urls:
            yield Request(url=url, callback=self.scry_phones)
    def scry_phones(self, response):
        phones = response.xpath('//div[@class="mw-category-group"]//li/a').extract()
        for phone in phones:
            matches = re.findall('href="(.*)" title="(.*)">', phone)
            for href, title in matches:
                uid = title.replace(' ', '_').encode('utf-8')
                url = 'https://en.wikipedia.org/w/index.php?title={}&action=edit'.format(uid)
                yield Request(url = url, callback=self.discover_phone, meta={'name':title})
    def discover_phone(self, response):
        code = response.xpath('//textarea/text()').extract()[0]
        currentphone = {}
        try:
            # TODO Continue from here
            data = re.findall(r'^\|(.*)', code, re.MULTILINE)
            print(data)
            #data = re.findall('{{Infobox Mobile phone(.*?)}}', code, re.DOTALL)[0]
            #print(data)
            #data = data.split('|')
            #data = filter(None, [entry.replace('\n','').strip() for entry in data])
            #data = [entry.split('=') for entry in data]
            #data = [entry for entry in data if len(entry) != 1]
            #for entry in data:
            #    entry = [value.strip().replace(' ','') for value in entry]
            #    entry[1] = entry[1].replace('[[','').replace(']]','')
            #    currentphone[entry[0]] = entry[1]
            #currentphone['name'] = response.meta['name']
            #self.phones.append(currentphone)
            #self.s += 1
            #sys.stdout.write(' {} '.format(self.s))
            #sys.stdout.flush()
            #print(currentphone)
        except Exception as e:
            pass
            #self.f += 1
            #sys.stdout.write('x')
            #sys.stdout.flush()
            #print(e)
            #self.missed.append(response.url)
    def spider_closed(self, spider):
        deduplicated = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in self.phones)]
        pprint.pprint(deduplicated)
        print("Wow, {} phones!".format(len(deduplicated)))
        print("I messed up {} articles.".format(len(self.missed)))
        print("Here they are: {}".format(self.missed))
        t = time.time()
        title = "crawl_{}.json".format(t)
        with open(title, "w") as file:
            json.dump(deduplicated, file)
