import scrapy
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from ..items import CatalogItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import lxml.html
import time

class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ["myeblaettle.de"]
    start_urls = ['https://www.myeblaettle.de/?group=1289']
    # path = "/Users/mr/Desktop/chromedriver"

    def __init__(self):
        # Web chrome init
        self.driver = webdriver.Chrome("/Users/mr/Desktop/chromedriver")

    def parse(self, response):
        page = self.driver.get(response.url)
        self.driver.find_element_by_xpath("//button[@id='cookieNoticeAcceptAllButton']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//a[@href='https://www.myeblaettle.de/frontend/getcatalog.do?catalogId=191056&catalogVersion=1&lang=de']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[href='/frontend/catalogs/191056/1/pdf/complete.pdf;jsessionid=2F24632DADB037CF007A188FA24E9CDA']").click()
        # find the element that we need to click
        print ()
        link_extraction = self.driver.find_element(By.ID, "sharing_sub_save")
# sharing_sub_save

        # print (page)
        # root = page_test.find_element_by_xpath("//a")
        # root = lxml.html.fromstring(page.get_html_source())
        yield {
        "html": link_extraction
        }

        # links = page.css("a")

        # for links in links:
        #     link_test = links.css("href").extract()
        #
        #     yield {
        #            "links" : link_test
        #            }

        # while True:
        #     next = self.driver.find_element_by_xpath("//button[@id='cookieNoticeAcceptAllButton']")
        #
        #     try:
        #         next.click()
        #
        #     except:
        #         pass
        #         # break
        #
        #     self.driver.close()
