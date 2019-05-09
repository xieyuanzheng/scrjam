import urllib.request
import re,ssl


for i in range(1,14):
    url="http://www.qiushibaike.com/hot/page/"+str(i)
    context = ssl._create_unverified_context()
    print("url : " + url)
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    data1 = urllib.request.Request(url, headers=headers)
    data = urllib.request.urlopen(url=data1, context=context).read().decode("utf-8", "ignore")
    pattern='<div class="content">\s+<span>\s+(.*?)\s+</span>\s+</div>'
    ssl._create_default_https_context = ssl._create_unverified_context
    contents=re.compile(pattern).findall(data)
    print(len(data))
    print(len(contents))
    try:
        for j in range(0,len(contents)):
            print(contents[j])
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        print(e)
    except Exception as e:
        print(e)