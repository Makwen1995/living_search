# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#直播Item
class LivingItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    host = scrapy.Field()
    url = scrapy.Field()
    channel = scrapy.Field()
    peopleNum = scrapy.Field()

#主播Item
class HostItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    followers = scrapy.Field()
    channel = scrapy.Field()
    url = scrapy.Field()


#结果Item
class ResultItem():
    name = scrapy.Field()
    abstract = scrapy.Field()
    url = scrapy.Field()
    keyword = scrapy.Field()
    subject_id = scrapy.Field()
    input_time = scrapy.Field()
    rule_id = scrapy.Field()
    uploader = scrapy.Field()