# -*- coding: utf-8 -*-
import scrapy,ssl
from scrjam.items import QiushiItem
from scrapy.http import Request


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    #start_urls = ['http://www.qiushibaike.com/hot/']

    def start_requests(self):
        header = {'User-Agent': 'User-Agent:Mozilla/5.0'}
        yield Request('http://www.qiushibaike.com/hot/',headers=header)

    def parse(self, response):
        context = ssl._create_unverified_context()
        ssl._create_default_https_context = ssl._create_unverified_context
        it = QiushiItem()
        it["content"] = response.xpath('//div[@class="content"]/span/text()').extract()
        it["link"] = response.xpath('//a[@class="contentHerf"]/@href').extract()
        yield it