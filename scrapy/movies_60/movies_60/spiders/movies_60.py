# Import modules
import scrapy

# Spider class for movies
# The conventon is to call, the class, after the domin it scrapes


class Movies_60Spider(scrapy.Spider):
    # Good practice is to name itafter the domain we trying to crawl.
    name = "movies_60"  # all lower case & name it as the page

    def start_request(self):  # requiered method requests sesion (start the sesio)
        urls = [
            'https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_1960s']

    def parse(self, response):  # required method extracts data
        # selectors
        all_listings = response.url.xpath("//table[@class='wikitable']")
        for data in all_listings:
            title_movies = data.xpath("//tr/td/i/a/@title")
            yield {
                "Title": title_movies
            }
    # def parse(self, response):
    #     page = response.url("/")[-2]
    #     filename = f'wiki-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

 # def parse(self, response):
 #        items = response.xpath("//div[@class='flash_li']")
 #        for product in items:
 #            product_name = product.xpath(".//a[@class='flash_li_link']/text()").get()
 #            product_sale_price = product.xpath(" .//div[@class='flash_li_price']/span/text()").get()
 #            product_org_price = product.xpath(".//div[@class='flash_li_price']/del/text()").get()
 #            product_url = product.xpath(".//a[@class='flash_li_link']/@href").get()
 #            discount =  product.xpath(".//div[@class='category_li_off']/text()").get()
 #             yield {
 #                    'name': product_name,
 #                    'sale_price': product_sale_price,
 #                    'orginal_price': product_org_price,
 #                    'url': product_url,
 #                    'discount': discount
 #             }
