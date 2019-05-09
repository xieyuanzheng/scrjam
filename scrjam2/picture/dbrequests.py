import requests
import re
from lxml import etree


#通过requests模拟登录豆瓣网
#https://blog.csdn.net/Stealth_pain/article/details/86768582

"""
    使用 request 模拟登录豆瓣，并获取用户名。
    在开发者工具的 network 选项卡中选中 preserve log 选项，然后输入用户名和错误的密码，找到登录时
    处理请求的 URL。
"""

class Login(object):
    def __init__(self):
        # 设置请求头
        self.headers = {
            #'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
            #'Host': 'accounts.douban.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        # 使用 requests.Session 模拟登录
        self.session = requests.Session()
        # 请求登录的 URL
        self.post_url = 'https://accounts.douban.com/j/mobile/login/basic'
        # 登录成功之后访问的 URL
        self.logined_url = 'https://accounts.douban.com/passport/setting'

    def login(self,name,password):
        # 登录时传递的表单数据
        post_data = {
            'ck': '',
            'name': "18680409093",
            'password': "db123456",
            'remember': False,
            'ticket': ''
        }
        # 使用 session 发起一个 POST 请求，并携带请求头和表单数据
        response = self.session.post(self.post_url,data=post_data,headers=self.headers)
        if response.status_code == 200:
            # 访问登录之后的页面
            response_logined = self.session.get(self.logined_url,headers=self.headers)
            html = etree.HTML(response_logined.text)
            # 获取并打印用户名
            print(html.xpath('//div[@class="account-form-field"]/input/@value')[0])
            print(html.xpath('//title//text()')[0])

def del_space(item):
    return re.sub(r'\s', '', item)


def main():
    login = Login()
    login.login('name', 'password')

if __name__ == "__main__":
    main()

