import scrapy
import requests
from urllib.parse import urlparse
# from scrapy_splash import SplashRequest
from selenium import webdriver

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

class MatadorSpider(scrapy.Spider):
    name = 'matador'
    start_urls = ["https://www.lokalmatador.de/epaper/lokalzeitung/wochenblatt-der-stadt-weil-der-stadt/"] #, "https://www.lokalmatador.de/epaper/lokalzeitung/deckenpfronner-wochenblatt/"]

    def __init__(self):
        path = "/Users/mr/Desktop/chromedriver"
        self.driver = webdriver.Chrome(path)

    def parse (self, response):
        self.driver.get(response.url)

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
    #     test = response.css("a[data-download-filename='weil-der-stadt_2021_29.pdf']::attr(href)").get()
    #     # print (type(test))
    #     print (test)
        # print (test.attrib['href'])
        # # print (response.css("a"))
        # for link in response.css("a"):
        #     print (link.attrib['href'])
        #     url = urlparse(response.url)
        #     print (url)
            # path = link.attrib['href']
            # print (url._replace(path=path).geturl())
            # print (path)
            # down_link = url.replace(path=path)
            # print (down_link)
