import scrapy
import requests
from ..items import FormItem

class Form_Post(scrapy.Spider):
    name = "form_post"
    # start_urls = ["https://www.wilkau-hasslau.de/bekanntmachungen/index.php"]
    start_urls = ["https://www.holzwickede.de/amtsblatt/index.php"]

    def parse(self, response):
        #Instance Variable
        items = FormItem()

        post = response.css("form[method=post]")

        for links in post:
            form = links.css("input[name='form']::attr(value)").extract()
            hash = links.css("input[name='hash']::attr(value)").extract()

            for link_site in self.start_urls:
                response_post = requests.post(link_site, params={'hash':hash, 'form': form})
                link = response_post.url

                # items["link"] = link
                items["form"] = form
                items["hash"] = hash
                items["link"] = link

            yield items
