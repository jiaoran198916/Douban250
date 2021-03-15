# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()
    quote = scrapy.Field()
    cover_url = scrapy.Field()
    introduce = scrapy.Field()