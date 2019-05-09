# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Request
from scrjam.items import doubanItem
from scrapy.http import FormRequest

#https://blog.csdn.net/qq_42293758/article/details/87925623
class Douban1Spider(scrapy.Spider):
    name = 'douban1'
    allowed_domains = ['douban.com']
    base_url = 'https://movie.douban.com/subject/1652592/comments?start={}&limit=20&sort=new_score&status=P'

    def start_requests(self):
        return [Request(url='https://movie.douban.com', meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        return FormRequest(
            url='https://accounts.douban.com/j/mobile/login/basic',
            method='POST',
            formdata={
                'ck': '',
                'name': '18680409093',
                'password': 'db123456',
                'remember': 'false',
                'ticket': ''
            },
            meta={'cookiejar': response.meta['cookiejar']},
            dont_filter=True,
            callback=self.after_login
        )

    def after_login(self, response):
        for i in range(22, 24):  # 20页之后的需要登陆之后才能访问
            url = self.base_url.format(i * 20)
            yield Request(url=url, meta={'cookiejar': 1}, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        results = response.css('div.comment-item')
        for result in results:
            item = doubanItem()
            item['user_nick'] = result.css('span.comment-info > a::text').extract_first()
            item['score'] = result.css('span.rating::attr(title)').extract_first()
            item['content'] = result.css('span.short::text').extract_first()
            item['userful_num'] = result.css('span.votes::text').extract_first()
            # print("开始爬虫")
            # print(item['user_nick'])
            # print(item['score'])
            # print(item['content'])
            # print(item['userful_num'])
            # print("结束爬虫")
            yield item
