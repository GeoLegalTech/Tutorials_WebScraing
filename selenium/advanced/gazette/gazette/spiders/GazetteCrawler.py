# -*- coding: utf-8 -*-
# Import Modules
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import scrapy

class GazetteSpider(scrapy.Spider):
    name = "Gazette"
    path = "/Users/mr/Desktop/chromedriver"
    url = "https://www.holzwickede.de/amtsblatt/index.php"

    def __init__(self):
        self.driver = webdriver.Chrome(path)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse (self, response):
        self.driver.get(url)
