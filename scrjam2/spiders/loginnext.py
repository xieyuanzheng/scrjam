# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest


class LoginnextSpider(scrapy.Spider):
    name = 'loginnext'
    allowed_domains = ['ufa.hk']
    start_urls = ['https://www.ufa.hk/mall/index.html']
    login_url = 'https://www.ufa.hk/mall/login.html'

    def parse(self, response):
        print("爬虫开始")
        print(response.text)
        return "haha"

    def start_requests(self):
        yield scrapy.http.Request(self.login_url, callback=self.login)

    def login(self, response):
        data = {
            "username": "18128682254",
            "password": "ufa123"
        }
        yield FormRequest.from_response(response, formdata=data, callback=self.login_parse)

    def login_parse(self, response):
        if "18128682254" in response.text:
            print("登录成功")
            print(response.url)
            yield self.start_requests()
            # yield from super.start_requests()
        else:
            print("打印respone")
            print(response.url)
            print("没有登录成功")
