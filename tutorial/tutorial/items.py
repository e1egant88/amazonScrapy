# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Products(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    sku = scrapy.Field()
    upc = scrapy.Field()
    ean = scrapy.Field()
    mpn = scrapy.Field()

class Reviews(scrapy.Item):
    user = scrapy.Field() 
    date = scrapy.Field()
    platform = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    rating = scrapy.Field()
    productname = scrapy.Field()

# class Categories(scrapy.Item):
#     categoryname = scrapy.Field()
#     productname = scrapy.Field()