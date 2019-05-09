# -*- coding: utf-8 -*-
import scrapy
from scrjam.items import BaiduItem


class QiushiSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        item = BaiduItem()
        item["title"] = response.xpath("/html/head/title/text()").extract()
        item["link"] = response.xpath("/html/head/title/text()").extract()
        yield item