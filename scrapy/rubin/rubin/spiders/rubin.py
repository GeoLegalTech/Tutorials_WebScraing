import json
import scrapy
import datetime
import requests
from ..items import RubinItem
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from dateutil.relativedelta import relativedelta

# Define functions

def get_years_months(my_date, num_months):
    cur_month = my_date.month
    cur_year = my_date.year

    result = []
    for i in range(num_months):
        if cur_month == 0:
            cur_month = 12
            cur_year -= 1
        result.append((cur_year, cur_month))
        cur_month -= 1

    return result

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

headers = get_headers('''
    name: GeOlegalTech
    value: Tests
    authority: www.lokalmatador.de
    :method: GET
    :path: /epaper/lokalzeitung/wochenblatt-der-stadt-weil-der-stadt/
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6
    cache-control: max-age=0
    cookie: sib_cuid=230d030a-1fa8-4740-9b3c-3d165026a68f; _fbp=fb.1.1628676200306.1767211144; _gid=GA1.2.2047125562.1629109458; lokalmatador-geo={"position":{"name":"Washington","lat":38.883333,"lon":-77,"accuracy":10,"ts":1629204349763},"status":true}; fe_typo_user=1ff8ee7099d8c8beb451a540221f0674; _dc_gtm_UA-101497132-5=1; _ga_K83HSJYRNW=GS1.1.1629374011.19.1.1629374136.0; _ga=GA1.1.2016523049.1628676200
    sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
    sec-ch-ua-mobile: ?0
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: none
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
    ''')

class Pagination(scrapy.Spider):
    name = 'pagination_rubin'
    start_urls = ["https://schifferstadt.more-rubin1.de/sitzungskalender.php"] # , "https://andernach.more-rubin1.de/sitzungskalender.php" , "https://schoenebeck.more-rubin1.de/sitzungskalender.php", "https://amt-sylt.more-rubin1.de/sitzungskalender.php", "https://stadtfehmarn.more-rubin1.de/sitzungskalender.php"]

    # # Make the asynchron stopping (Requests one by one)
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 0,                    #Secs
    #     'CONCURRENT_REQUESTS_PER_DOMAIN': 1    #Secs
    # }

    def __init__(self):
        # pass
        print (self.start_urls)
        new_starturl = []
        for new_link in self.start_urls:
            trial_url = urlparse(new_link)
            print (trial_url)
            trial_url =  trial_url._replace(path="calendar.php?month=2021-10")
            base_url = trial_url.geturl()
            print (base_url)
            months = get_years_months(datetime.date.today(), 1)
            # print (datetime.date.april())
            print (months)
            for month in months:
                (month, day) = month
                if len(str(day)) == 1:
                    day = "0" + str(day)
                else:
                    day
                new_date = str(month) + "-" + str(day)
                url = urlparse(base_url)
                old_date = url.query.split('=')[1]
                parts = url.query
                parts = parts.replace(old_date, new_date)
                url = url._replace(query=parts)
                url = url.geturl()
                new_starturl.append(url)
                self.start_urls = new_starturl

            # for link in self.start_urls:
            #     if link is not None:
            #         yield scrapy.Request(url=link, callback=self.parse)

        # Control flag
        # print (self.start_urls)



    def parse(self, response):
        # pass
        print('response url:', response.url) #Control flag
        print (response.body)
        # div:nth-of-type(2) > .calendar-page-day-content > div > a > .calendar-page-day-meeting > .calendar-page-day-meeting-title
        #
        # post = response.css("")
        # print (post)
        # hash = post.css("input[name='sid']::attr(value)").extract()

        # for link in hash:
        #     parse_url = urlparse(response.url)
        #     parse_url = parse_url._replace(path="sitzungen_top.php")
        #     parse_url = parse_url._replace(query="sid=")
        #     parse_url = parse_url.geturl()
        #     parse_url = parse_url + link
        #     print ("Test URL: ")
        #     print (parse_url)
        #
        #     # for link in parse_url:
        #     if parse_url is not None:
        #         yield scrapy.Request(parse_url, callback=self.parse_doc)

        # get = response.css("form[method=get]")
        # sid = get.css("input[name='sid']::attr(value)").extract()
        # for link in sid:
        #     parse_url = urlparse(response.url)
        #     parse_url = parse_url._replace(path="meeting.php")
        #     parse_url = parse_url._replace(query="sid=")
        #     parse_url = parse_url.geturl()
        #     parse_url = parse_url + link
        #     # print (parse_url)
        #
        #     if parse_url is not None:
        #         yield scrapy.Request(parse_url, callback=self.parse_api)


    # def parse_doc(self, response):
    #
    #     items = RubinItem()
    #
    #     get = response.css("form[method=get]")
    #     for links in get:
    #         parse_url = urlparse(response.url)
    #         typ = links.css("input[name='_typ_432']::attr(value)").get()
    #         doc = links.css("input[name='_doc_n1']::attr(value)").get()
    #         nk  = links.css("input[name='_nk_nr']::attr(value)").get()
    #         nid = links.css("input[name='_nid_nr']::attr(value)").get()
    #         neu = links.css("input[name='_neu_dok']::attr(value)").get()
    #         stat = links.css("input[name='status']::attr(value)").get()
    #         sitzung = links.css("input[name='sitzungsnummer']::attr(value)").get()
    #         params = {
    #         '_typ_432' : typ,
    #         '_doc_n1' : doc,
    #         '_nk_nr' : nk,
    #         '_nid_nr': nid,
    #         '_neu_dok':neu,
    #         'status': stat,
    #         'sitzungsnummer' : sitzung
    #         }
    #         site_path = "/show_pdf.php"
    #         parse_url = urlparse(response.url)
    #         site_url = parse_url.scheme + '://' + parse_url.netloc + site_path
    #         link = requests.post(site_url, params=params)
    #         link = link.url
    #
    #         items["link"] = link
    #
    #         yield items
    #
    # def parse_api(self, response):
    #
    #     items = RubinItem()
    #
    #     div = response.css("div[id='content']")
    #     for links in div:
    #         querys = links.xpath("//script/text()").re(r'document_type_id+=\d+&[a-zA-Z]+[_a-zA-Z]+=[a-zA-Z_\d\w\.\-\%\&\=]+')
    #         ''' Old system '''
    #         # print (len(links.xpath("//script/text()").getall()))
    #         # querys = links.css("div[component='MeetingPage']::attr(vue-passed-meeting)").re(r'document_type_id+=\d+&[a-zA-Z]+[_a-zA-Z]+=[a-zA-Z_\d\w\.\-\%\&\=]+')
    #         ''' Old system '''
    #         for query_new in querys:
    #             parse_url = urlparse(response.url)
    #             parse_url = parse_url._replace(path="documents.php")
    #             parse_url = parse_url._replace(query=query_new)
    #             parse_url = parse_url.geturl()
    #             link = parse_url
    #             print (link)
    #             # print (type(parse_url))
    #
    #             items["link"] = link
    #             yield items
