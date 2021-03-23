import json
import scrapy
import requests
from datetime import datetime
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess

# Define functions
def get_headers(s, sep=': ', strip_cookie=False, strip_cl=True, strip_headers: list = []) -> dict():
    """ Function adapted and taken from GitHub """
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d

class Pagination(scrapy.Spider):
    name = 'pagination_rubin'
    start_urls = ["https://schifferstadt.more-rubin1.de/sitzungskalender.php"] #, "https://schoenebeck.more-rubin1.de/sitzungskalender.php", "https://amt-sylt.more-rubin1.de/sitzungskalender.php", "https://andernach.more-rubin1.de/sitzungskalender.php"]
    headers = get_headers('''
        Accept: */*
        Accept-Encoding: gzip, deflate, br
        Accept-Language: en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6
        Connection: keep-alive
        Cookie: JSESSIONID=1C8FB6174CE3B4A7E3D827033026D902; _ga=GA1.2.416603156.1614336675; _gid=GA1.2.567457664.1614593357; _gat=1
        Host: www.myeblaettle.de
        Referer: https://www.myeblaettle.de/
        sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
        sec-ch-ua-mobile: ?0
        Sec-Fetch-Dest: empty
        Sec-Fetch-Mode: cors
        Sec-Fetch-Site: same-origin
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36
        X-Requested-With: XMLHttpRequest
        ''')

    # # Make the asynchron stopping (Requests one by one)
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 0,                    #Secs
    #     'CONCURRENT_REQUESTS_PER_DOMAIN': 1    #Secs
    # }

    def __init__(self):

        new_starturl = []
        for new_link in self.start_urls:
            trial_url = urlparse(new_link)
            trial_url =  trial_url._replace(query="skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft=")
            base_url = trial_url.geturl()
            for month_num in range(1, 4):
                url = urlparse(base_url)
                month = url.query.split('=')[3].split('&')[0].split('-')[1]
                parts = url.query
                parts = parts.replace(month, "0" + str(month_num))
                url = url._replace(query=parts)
                url = url.geturl()
                new_starturl.append(url)
                self.start_urls = new_starturl
        # Control flag
        # print (self.start_urls)

        # https://schifferstadt.more-rubin1.de/meeting.php?sid=ni_2021-02-129

    def parse(self, response):
        # print('response url:', response.url) #Control flag
        get = response.css("form[method=get]")
        for link_site in self.start_urls:
            for links in get:
                form = links.css("input[name]::attr(value)").extract()
                hash = links.css("input[name='sid']::attr(value)").extract()
                print (form)
                print (hash)

        # print (post)


# run scraper
process = CrawlerProcess()
process.crawl(Pagination)
process.start()
