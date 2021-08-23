import scrapy


class Matador2Spider(scrapy.Spider):
    name = 'matador2'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
