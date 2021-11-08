import scrapy
import requests
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from scrapy_splash import SplashRequest
from scrapy.crawler import CrawlerProcess
from pyshadow.main import Shadow

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

class MatadorSpider(scrapy.Spider):
    name = 'matador'
    start_urls = ["https://www.lokalmatador.de/epaper/ausgabe/wochenblatt-der-stadt-weil-der-stadt-29-2021/"]#["https://www.lokalmatador.de/epaper/lokalzeitung/wochenblatt-der-stadt-weil-der-stadt/"] #, "https://www.lokalmatador.de/epaper/lokalzeitung/deckenpfronner-wochenblatt/"]

    def __init__(self):
        path = "/Users/mr/Desktop/chromedriver"
        self.driver = webdriver.Chrome(path)

    def parse (self, response):
        # cookie = headers
        # self.driver.add_cookie(cookie)
        self.driver.get(response.url)
        # pdf = self.driver.find_element_by_link_text("PDF herunterladen")
        # pdf.click()
        self.driver.implicitly_wait(10)
        item = self.driver.execute_script("return document.querySelector('#usercentrics-root').shadowRoot.querySelector('button[data-testid=uc-accept-all-button]')")   # .shadowRoot.querySelector('div')")
        print ("This is an item")
        print (item)
        item.click()
        test = self.driver.find_element_by_css_selector("a[data-download-filename='weil-der-stadt_2021_29.pdf']").get_attribute("href")
        print (test)
        print (self.driver.find_element_by_css_selector("a[data-download-filename='weil-der-stadt_2021_29.pdf']").get_attribute("href"))
        test.click()
        # element = WebDriverWait(self.driver, 10).until(
        # EC.presence_of_element_located((By.LINK_TEXT, "PDF herunterladen"))
        # )
        # element.click()

        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "PDF herunterladen"))
        #     )
        #     element.click()
        #     # print (element)
        # finally:
        #     self.driver.quit()



        # Shadow
        # shadow = Shadow(self.driver)
        # shadow.set_implicit_wait(10)
        # element = shadow.find_element("p#btn-group-custom>button#Alles akzeptieren")


        # self.driver.quit()
        # cookie = headers
        # # # print (cookie)
        # self.driver.add_cookie(cookie)
        # self.driver.get_cookies()
        # try:
        #     element = WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "Alle akzeptieren"))
        #     )
        #     # element.click()
        #     print (element)
        # finally:
        #     self.driver.quit()

        # print (test)

    # def parse(self, response):
    #     for new_link in self.start_urls:
    #         trial_url = urlparse(new_link)
    #         href = response.css("a[target='_self']")
    #         for link in href:
    #             path = link.attrib['href']
    #             n_url =  trial_url._replace(path=path)
    #             n_url = n_url.geturl()
    #             if n_url is not None:
    #                 yield SplashRequest(n_url, callback=self.download_doc)
    #
    #     # Control point
    #     # print (self.start_urls)
    #
    # def download_doc(self, response):
    #     # print (response.body)
    #     # print (response.headers)
    #     # print ("This is the response")
    #     # print (response.css("a[data-download-filename='weil-der-stadt_2021_28.pdf']"))
    #     # test = response.css("a[data-download-filename='weil-der-stadt_2021_28.pdf']")
    #     # print (test.attrib['href'])
    #     # # print (response.css("a"))
    #     for link in response.css("a"):
    #         print (link.attrib['href'])
    #         url = urlparse(response.url)
    #         print (url)
    #         path = link.attrib['href']
    #         print (url._replace(path=path).geturl())
    #         # print (path)
    #         # down_link = url.replace(path=path)
    #         # print (down_link)

# run scraper
process = CrawlerProcess()
process.crawl(MatadorSpider)
process.start()


# 744d29e8dd1fc082f4fa1b316cc3f63f
# # # 28
# vv821f6vrbb7w2zfe3w8u4pe
# # https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=013e1c3a09e5099cdfbd5ca7714ba0e9
# https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=2907018c8a15d8812ecb22b22c27baee&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=d2a81a9e45a560fb6c844d624b5c569f&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# #
# # https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=e0aecbf00dda01cec40ed1d7a0d34364&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# # https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=a1344f042c668acba68af6b8fccd62d7&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# # /index.php?id=151&amp;tx_epaper_epaperdetail%5BdownloadHashKey%5D=a1344f042c668acba68af6b8fccd62d7&amp;tx_epaper_epaperdetail%5Baction%5D=checkHash&amp;tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# # # # https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=a9d1741d527dbc514c30117c2d6737cd&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# # # https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=e397165a71497736b4a70adf2385e4f0&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# # https://www.lokalmatador.de/index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=a1344f042c668acba68af6b8fccd62d7&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# # /index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=20744198d2d4ba1c16e2bac408f1f9ea&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt
# # # /index.php?id=151&tx_epaper_epaperdetail%5BdownloadHashKey%5D=20744198d2d4ba1c16e2bac408f1f9ea&tx_epaper_epaperdetail%5Baction%5D=checkHash&tx_epaper_epaperdetail%5Bcontroller%5D=Amtsblatt"
