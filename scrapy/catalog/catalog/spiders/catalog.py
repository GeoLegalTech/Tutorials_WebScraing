import scrapy
import requests
from ..items import CatalogItem

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

class CatalogSpider(scrapy.Spider):
    name = "catalog"
    start_urls = ["https://www.myeblaettle.de/?group=1289"]

    def parse(self, response):

        #Instance Variable for database
        items = CatalogItem()

        # Execute when its a post method
        post = response.css("a")

        yield {"link" : post}

        # for link_site in self.start_urls:
        #
        #     for links in post:
        #     # Extraction values to push
        #         form = links.css("input[name='form']::attr(value)").extract()
        #         hash = links.css("input[name='hash']::attr(value)").extract()
        #
        #         # Push the request parameters & get url
        #         response_post = requests.post(link_site, params={'hash':hash, 'form': form})
        #         link = response_post.url
        #
        #         items["form"] = form
        #         items["hash"] = hash
        #         items["link"] = link
        #
        #         yield items
