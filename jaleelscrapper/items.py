# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JaleelscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    destination, = scrapy.Field()
    time = scrapy.Field()
    temperature = scrapy.Field()
    note = scrapy.Field()

