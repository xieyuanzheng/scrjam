# -*- coding: utf-8 -*-
import scrapy
from scrjam.items import ScrjamItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        print("这是一个爬虫的开始,增加webbook钉钉机器人通知")
        item = ScrjamItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        item['link'] = response.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[2]/a/@href').extract()
        item['desc'] = response.xpath('/html/body/div[1]/div[12]/div/div[1]/p/text()').extract()
        print(item['link'])
        print("这是一个爬虫的结束")
        yield item