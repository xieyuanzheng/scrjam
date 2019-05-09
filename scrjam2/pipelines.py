# -*- coding: utf-8 -*-
from scrapy.crawler import Settings as settings
import pymysql,ssl
from twisted.enterprise import adbapi


class ScrjamPipeline(object):
    def __init__(self):
        self.fh = open("/Users/apple/Desktop/work/project/python/scrjam/scrjam/ts.txt","a+")

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        print("开始爬虫---")
        print(item["title"])
        print(item["link"])
        print(item["stu"])
        print("结束爬虫")
        self.fh.write(item["title"][0]+"\n"+item["stu"][0]+"\n"+"-----"+"\n")
        return item

    def close_spider(self, spider):
        self.fh.close()


class MysqlPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        # 从项目的配置文件中读取相应的参数
        cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'scrapy_db')
        cls.HOST = crawler.settings.get("MYSQL_HOST", '47.104.108.184')
        cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
        cls.USER = crawler.settings.get("MYSQL_USER", 'pwpw1218')
        cls.PASSWD = crawler.settings.get("MYSQL_PASSWORD", 'Pwpw1218@**!')
        return cls()

    def open_spider(self, spider):
        self.dbpool = adbapi.ConnectionPool('pymysql', host=self.HOST, port=self.PORT, user=self.USER,
                                            passwd=self.PASSWD, db=self.MYSQL_DB_NAME, charset='utf8')

    def close_spider(self, spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        print(item["content"][0])
        self.dbpool.runInteraction(self.insert_db, item)

        return item

    def insert_db(self, tx, item):
        values = (
            item['content'],
            item['link'],
        )
        print("开始执行SQL")
        sql = 'INSERT INTO qiushi (content,link) VALUES (%s,%s)'
        tx.execute(sql, values)
        print("结束执行SQL")


class DoubanPipeline(object):
    def __init__(self):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        print("开始爬虫---")
        print(item['user_nick'])
        print("结束爬虫")
        return item

    def close_spider(self, spider):
        pass