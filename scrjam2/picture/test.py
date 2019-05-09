import urllib.request
import ssl,re

# keyname="短裙"
# key=urllib.request.quote(keyname)
url="http://blog.csdn.net"
#headers=("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
# opener=urllib.request.build_opener()
# opener.addheaders=[headers]
# opener=urllib.request.install_opener(opener)
context = ssl._create_unverified_context()
#req=urllib.request.Request(url=url,headers=headers)
data=urllib.request.urlopen(url,context=context).read().decode("utf-8","ignore")
print(len(data))
pat='<span class="num">(\d+)</span>'
result=re.compile(pat).findall(data)
print(result)
fh = open("/Users/apple/Desktop/work/project/python/picture/picture/num.txt","w")
for i in range(0,len(result)):
    print(result[i])
    fh.write(result[i]+"\n")
fh.close()
# for i in range(0,3):
#     "网址拼接"
#     data=urllib.request.urlopen("").read().decode("utf-8","ignore")
#     pat='pic_url:"(.*?)"'
#     imagelist=re.compile(pat).findall(data)
#     for j in range(0,len(imagelist)):
#         thisimg=imagelist[j]
#         imgurl="http://"+thisimg
#         file="/Users/apple/Desktop/work/project/python/picture/picture/"+str(i)+str(j)+".jpg"
#         urllib.request.urlsplit(imgurl,filename=file)