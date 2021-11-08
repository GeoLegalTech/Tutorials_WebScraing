import scrapy
import datetime
import requests
from selenium import webdriver
from pyshadow.main import Shadow
from urllib.parse import urlparse
from scrapy_splash import SplashRequest
from scrapy.crawler import CrawlerProcess
from selenium.webdriver.common.by import  By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    start_urls = ["https://schoenebeck.more-rubin1.de/sitzungskalender.php", "https://andernach.more-rubin1.de/sitzungskalender.php" , "https://schoenebeck.more-rubin1.de/sitzungskalender.php", "https://amt-sylt.more-rubin1.de/sitzungskalender.php", "https://stadtfehmarn.more-rubin1.de/sitzungskalender.php"]

    # # Make the asynchron stopping (Requests one by one)
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 0,                    #Secs
    #     'CONCURRENT_REQUESTS_PER_DOMAIN': 1    #Secs
    # }

    def __init__(self):
        # pass
        ''' Local test, no binary '''
        # path = "/Users/mr/Desktop/chromedriver"
        # self.driver = webdriver.Chrome(path)

        ''' Server Test, binary '''
        # path = "/usr/local/bin/chromedriver"
        s = Service(path)
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service = s, options=chrome_options)

        new_starturl = []
        for new_link in self.start_urls:
            trial_url = urlparse(new_link)
            trial_url =  trial_url._replace(path="calendar.php?month=2021-10")
            base_url = trial_url.geturl()
            months = get_years_months(datetime.date.today(), 2)
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
                # print (" --------- These are my monthly urls ---------")
                # print (url)
                # Start Chromedriver to parse href
                self.driver.get(url)
                item = self.driver.find_elements_by_class_name('calendar-page-day-content')
                for i in item:
                    ele = self.driver.find_elements(By.TAG_NAME, "a")
                for link in ele:
                    new_starturl.append(link.get_attribute("href"))
                    # Delete information not desire
            # print ("------- This is my new href from the months -------")
            # print (new_starturl)
            # Clean no meetings
            n_list = []
            for l in new_starturl:
                if l is not None:
                    if "meeting" in l:
                        n_list.append(l)
            self.start_urls = n_list

    def parse(self, response):
        # pass
        print (' ----- This is my URL -----')
        # print (self.url)
        print (response.url)
        div = response.css("div[id='content']")
        for links in div:
            querys = links.xpath("//script/text()").re(r'document_type_id+=\d+&[a-zA-Z]+[_a-zA-Z]+=[a-zA-Z_\d\w\.\-\%\&\=]+')
            ''' Old system '''
                    # print (len(links.xpath("//script/text()").getall()))
                    # querys = links.css("div[component='MeetingPage']::attr(vue-passed-meeting)").re(r'document_type_id+=\d+&[a-zA-Z]+[_a-zA-Z]+=[a-zA-Z_\d\w\.\-\%\&\=]+')
            ''' Old system '''
            for query_new in querys:
                parse_url = urlparse(response.url)
                parse_url = parse_url._replace(path="documents.php")
                parse_url = parse_url._replace(query=query_new)
                parse_url = parse_url.geturl()
                print (parse_url)

# run scraper
process = CrawlerProcess()
process.crawl(Pagination)
process.start()
