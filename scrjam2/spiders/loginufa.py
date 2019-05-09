# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest


class LoginufaSpider(scrapy.Spider):
    name = 'loginufa'
    allowed_domains = ['ufa.hk']
    #start_urls = ['https://www.ufa.hk/mall/index.html']
    login_url = 'https://www.ufa.hk/mall/login.html'
    header = {
    "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def start_requests(self):
        return [scrapy.http.Request(self.login_url, callback=self.parse, meta={"cookiejar": 1})]

    def parse(self, response):
        print("爬虫开始")
        data={
                "username":"18128682254",
                "password":"ufa123"
            }
        return [FormRequest.from_response(response,
                                         formdata=data,
                                         callback=self.login_parse,
                                         headers=self.header,
                                         meta={"cookiejar":response.meta["cookiejar"]})]

    def login_parse(self,response):
        if "18128682254" in response.text:
            print("登录成功")
            print(response.url)
            #yield self.start_requests()
            #yield from super.start_requests()
        else:
            print("打印respone")
            print(response.url)
            print("没有登录成功")