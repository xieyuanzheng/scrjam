# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrjamItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class BaiduItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()


class QiushiItem(scrapy.Item):
    content = scrapy.Field()
    link = scrapy.Field()


class QsautoItem(scrapy.Item):
    content = scrapy.Field()
    link = scrapy.Field()


class tsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    stu = scrapy.Field()


class doubanItem(scrapy.Item):
    user_nick = scrapy.Field()
    score = scrapy.Field()
    content = scrapy.Field()
    userful_num = scrapy.Field()
