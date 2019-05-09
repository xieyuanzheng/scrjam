# -*- coding: utf-8 -*-
import scrapy
from scrjam.items import tsItem
from scrapy.http import Request

#爬起下一页内容
class TsSpider(scrapy.Spider):
    name = 'ts'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        it = tsItem()
        it["title"] = response.xpath('/html/body/div[2]/div[1]/div/div[2]/div/h1/text()').extract()
        it["link"] = response.xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div/h1[2]/a/@href').extract()
        it["stu"] = response.xpath('/html/body/div[2]/div[1]/div/div[2]/div/div[2]/span[2]/text()').extract()
        yield it

        for i in range(1,6):
            url = 'https://edu.hellobi.com/course/' + str(i)
            #Request表示进行访问一次
            yield Request(url,callback=self.parse)
