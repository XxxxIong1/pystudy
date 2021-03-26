import urllib.request
import urllib

#1，网站url
url = 'http://www.baidu.com'

#2.创建request请求对象
request = urllib.request.Request(url)

#3.发送请求获取结果
response = urllib.request.urlopen(request)
htmldata = response.read()

#4.设置编码方式
htmldata = htmldata.decode('utf-8')

#打印结果
print(htmldata)

#打印爬去网页的各类信息
print("response的类型:",type(response))
print("请求的url:",response.geturl())
print("响应的信息:",response.info())
print("状态码:",response.getcode())

#7.爬取数据保存到文件
fileOb = open('baidu.html','w',encoding='utf-8')
fileOb.write(htmldata)
fileOb.close()