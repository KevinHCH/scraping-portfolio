# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LondonhousingItem(scrapy.Item):
    url = scrapy.Field()
    district = scrapy.Field()
    total_houses = scrapy.Field()
    address = scrapy.Field()
    property_type = scrapy.Field()
    has_floor_plan = scrapy.Field()
    transactions = scrapy.Field()
    location = scrapy.Field()
    pass
