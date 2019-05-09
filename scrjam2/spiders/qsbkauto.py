# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrjam.items import QsautoItem


class QsbkautoSpider(CrawlSpider):
    name = 'qsbkauto'
    allowed_domains = ['paison.top']

    start_urls = ['http://www.paison.top:8996/']

    # def start_requests(self):
    #     header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    #     yield Request('https://www.ufa.hk/mall/index.html', headers=header)


    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        it = QsautoItem()
        #it["content"] = response.xpath('//div[@class="content"]/span/text()').extract()
        it["link"] = response.xpath('//*[@id="THEME_MARKET"]/ul/li[1]/ol/li[2]/a/@href').extract()
        print("爬虫开始。。。。。。")
        print("爬虫结束。。。。。。")
        return it
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #return item

