import scrapy
from scrapy.utils.response import open_in_browser

# function

def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
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

class CataloBasicSpider(scrapy.Spider):
    name = 'catalo_basic'
    # allowed_domains = ['s']
    # start_urls = ['http://s/']

    def start_requests(self):
        h = get_headers('''
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Accept-Encoding: gzip, deflate, br
        Accept-Language: en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6
        Cache-Control: max-age=0
        Connection: keep-alive
        Cookie: _ga=GA1.2.1973768868.1614089083
        Host: www.myeblaettle.de
        If-Modified-Since: Tue, 12 Jan 2021 15:07:30 GMT
        If-None-Match: W/"5ffdbb32-16d9"
        sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
        sec-ch-ua-mobile: ?0
        Sec-Fetch-Dest: document
        Sec-Fetch-Mode: navigate
        Sec-Fetch-Site: none
        Sec-Fetch-User: ?1
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36

        ''')
        req = scrapy.Request("https://www.myeblaettle.de/?group=1289", headers=h)
        yield (req)

    def parse(self, response):
        post = response.css("span")
        yield {"post" : post}
        # print (response)
