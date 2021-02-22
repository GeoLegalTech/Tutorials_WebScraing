# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data into a database

import scrapy


class FormItem(scrapy.Item):
    # define the fields for your item here like:
    form = scrapy.Field()
    hash = scrapy.Field()
    
