import scrapy
import requests
from ..items import FormItem

class Form_Post(scrapy.Spider):
    name = "form_post"
    # start_urls = ["https://www.wilkau-hasslau.de/bekanntmachungen/index.php"]
    start_urls = [
    "https://www.holzwickede.de/amtsblatt/index.php",
    "https://www.wilkau-hasslau.de/bekanntmachungen/index.php"
    ]

    # for links_web in start_urls:
    #     yield links_web

    def parse(self, response):

        #Instance Variable for database
        items = FormItem()

        # Execute when its a post method
        post = response.css("form[method=post]")

        for link_site in self.start_urls:

            for links in post:
            # Extraction values to push
                form = links.css("input[name='form']::attr(value)").extract()
                hash = links.css("input[name='hash']::attr(value)").extract()

                # Push the request parameters & get url
                response_post = requests.post(link_site, params={'hash':hash, 'form': form})
                link = response_post.url

                items["form"] = form
                items["hash"] = hash
                items["link"] = link

                yield items
