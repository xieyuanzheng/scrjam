import urllib.request
import re,ssl

url1="https://www.ufa.hk/mall/mod/search.html?st=1&sk=&pageNo=1"
url2="https://www.ufa.hk/mall/mod/search.html?st=1&sk=&pageNo=2"
url3="https://www.ufa.hk/mall/mod/search.html?st=1&sk=&pageNo=3"
image_url="https://www.ufa.hk/uploads/ufa/gds/GoodsVO/2018/07/07/wzDmnABCQemHePEA7x0vGA.jpeg"


for i in range(1,5):
    url = "https://www.ufa.hk/mall/mod/search.html?st=1&sk=&pageNo="+str(i)
    context = ssl._create_unverified_context()
    data = urllib.request.urlopen(url,context=context).read().decode("utf-8","ignore")
    print(len(data))
    pat = '<img src=".*?" data-echo="(.*?[.png|.jpg|.jpeg])"\s+onerror=".*?"/>'
    image_re = re.compile(pat).findall(data)
    for j in range(0, len(image_re)):
        try:
            print("图片链接地址为："+image_re[j])
            filename = "/Users/apple/Desktop/work/project/python/picture/picture/411/"+str(i)+str(j)+".jpg"
            ssl._create_default_https_context = ssl._create_unverified_context
            data_save = urllib.request.urlretrieve(image_re[j], filename=filename)
            print("第"+str(i)+str(j)+"次爬虫成功")
        except urllib.error.URLError as e:
            print("爬虫失败")
            print(e)
            if hasattr(e,"code"):
                print(e.code)