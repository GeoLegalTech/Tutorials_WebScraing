import scrapy

# Spider class for movies
class movies_60(scrapy.Spider):
    name = "movies_60" #all lower case & name it as the page

    def start_request(self):    #requiered method requests sesion
    urls = ['https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_1960s']

    for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response): #required method extracts data
    #selectors
    all_listings = response.xpath()
