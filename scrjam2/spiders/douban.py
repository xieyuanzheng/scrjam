# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    #start_urls = ['http://www.douban.com/']
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    #login_url = 'https://www.douban.com/'
    header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def start_requests(self):
        return [Request(self.login_url,callback=self.parse,meta={"cookiejar":1})]

    def parse(self, response):
        print("此时没有验证码")
        data={
            'ck': '',
            'name': "18680409093",
            'password': "db123456",
            'remember': False,
            'ticket': ''
        }
        print("登录中.....")
        return [FormRequest.from_response(response,
                                          meta={"cookiejar":response.meta["cookiejar"]},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next)]

    def next(self,response):
        print("此时已经登录完成，并爬取个人中心的数据")
        print(response.status_code)
        title = response.xpath("/html/head/title/text()").extract()
        content = response.xpath('//*[@id="statuses"]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/a/text()').extract()
        print(title[0])
        print(content[0])
        print("爬虫结束")