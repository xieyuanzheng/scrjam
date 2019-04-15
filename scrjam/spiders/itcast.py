# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        print("这是一个爬虫的开始")
        pass
