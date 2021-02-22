import scrapy
import requests
from ..items import FormItem

class Form_Post(scrapy.Spider):
    name = "form_post"
    start_urls = ["https://www.holzwickede.de/amtsblatt/index.php"]

    def parse(self, response):
        #Instance Variable
        items = FormItem()

        post = response.css("form[method=post]")

        for links in post:
            form = links.css("input[name='form']::attr(value)").extract()
            hash = links.css("input[name='hash']::attr(value)").extract()

            items["form"] = form
            items["hash"] = hash

            yield items






            # response_post = requests.post(start_urls, params={'hash':hash, 'form': form})
            # link = response_post.url

            # form = links.xpath("//input[@name='form']/@value").extract()
            # hash = links.xpath("//input[@name='hash']/@value").extract()

#         form class=put
# response.css("form[method=post]").xpath("//input[@name='form']/@value").get()
# # response = requests.get(url, params={'key1': 'value1', 'key2': 'value2'})
# # print (response.url)
# response.xpath("//td/form/input/name='hash'/@value").getall()
# response.xpath("//input[@name='hash']/@value").getall()
# request.
# if hash and name are equal, then
