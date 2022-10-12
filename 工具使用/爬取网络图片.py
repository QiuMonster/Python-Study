import random
import urllib.request  # 导入用于打开URL的扩展库模块
import urllib.parse
import re  # 导入正则表达式模块


def open_url(url,imgName,pack):
    req = urllib.request.Request(url)  # 将Request类实例化并传入url为初始值，然后赋值给req
    # 添加header，伪装成浏览器
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
    # 访问url，并将页面的二进制数据赋值给page
    try:
        page = urllib.request.urlopen(req)
        # 将page中的内容转换为utf-8编码
        html = page.read()  # .decode('utf-8')
        get_img(html, imgName,pack)
        print(imgName)
        # print(html)
        # return html
    except:
        print("no"+imgName)
        pass



def getImgName(url):
    req = urllib.request.Request(url)  # 将Request类实例化并传入url为初始值，然后赋值给req
    # 添加header，伪装成浏览器
    req.add_header('User-Agent'
                   ,
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
    # 访问url，并将页面的二进制数据赋值给page
    page = urllib.request.urlopen(req)
    # 将page中的内容转换为utf-8编码
    html = page.read()  # .decode('utf-8')
    # [ ^ "]+\.jpg 匹配除"
    # 以外的所有字符多次, 后面跟上转义的.和png
    name = r'"([^"]+\.jpeg)"'
    #   p=r'<img src="([^"]+\.png)"'
    #   #返回正则表达式在字符串中所有匹配结果的列表
    imglist = re.findall(name, html)
    # print(imglist)
    return html


def get_img(html, name,pack):
    f = open('G:/Python爬取的图片/'+pack+'/' + name + '.jpeg', 'wb')
    # 写入获取的数据
    f.write(html)
    # 关闭文件
    f.close()


# 该模块既可以导入到别的模块中使用，另外该模块也可自我执行
if __name__ == '__main__':
    # getImgName("https://www.pexels.com/zh-cn/search/%E6%97%A5%E8%90%BD/")
    for i in range(1000):
        name = str(int(10000000 * random.random()))
        url = "https://images.pexels.com/photos/" + name + "/pexels-photo-" + name + ".jpeg"
        pack="pexels3"
        open_url(url, name,pack)
        print(i)

    # get_img(data, "1")
    # for i in range(10):
    #     name = str(int(10000000 * random.random()))
    #     # name = str(0 + i)
    #     url = "https://images.pexels.com/photos/" + name + "/pexels-photo-" + name + ".jpeg"
    #     open_url(url, name)
    #     # try:
    #     #     open_url(url, name)
    #     #     # print(name)
    #     # except:
    #     #     print("no"+i)
    #     #     pass

# # -*- coding: utf-8 -*-
# import urllib3
# import re
# def main():
#   # 利用urllib2的urlopen方法，下载当前url的网页内容
#   req = urllib3.urlopen('https://images.pexels.com/photos/4245825/pexels-photo-4245825.jpeg')
#   # 将网页内容存储到buf变量中
#   buf = req.read()
#   # 将buf中的所有内容与需要匹配的url进行比对。这里的正则表达式是根据静态网页的源码得出的，查看静态网页源码开启开发者模式，按F12即可。然后确定图片块，查看对应源码内容，找出规律，编写正则表达式。
#   listurl = re.findall(r'src=.+\.jpeg',buf)
#   i = 0
#   # 将结果循环写入文件
#   for url in listurl:
#     f = open(str(i)+'.jpg','w')
#     req = urllib3.urlopen(url[5:])
#     buf1 = req.read()
#     f.write(buf1)
#     i+=1
# if __name__ == '__main__':
#   main()


# import urllib .request  #导入用于打开URL的扩展库模块
# import urllib .parse
# import re    #导入正则表达式模块
#
# def open_url(url):
#   req=urllib .request .Request (url)   #将Request类实例化并传入url为初始值，然后赋值给req
#   #添加header，伪装成浏览器
#   req.add_header('User-Agent'
#                  ,'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
#   #访问url，并将页面的二进制数据赋值给page
#   page=urllib .request .urlopen(req)
#   #将page中的内容转换为utf-8编码
#   html=page .read().decode('utf-8')
#
#   return html
#
# def get_img(html):
#   # [^"]+\.jpg 匹配除"以外的所有字符多次,后面跟上转义的.和png
#   p=r'<img src="([^"]+\.png)"'
#   #返回正则表达式在字符串中所有匹配结果的列表
#   imglist=re.findall(p,html )

#   #循环遍历列表的每一个值
#   for each in imglist :
#     #以/为分隔符，-1返回最后一个值
#     filename=each.split("/")[-1]
#     # 访问each，并将页面的二进制数据赋值给photo
#     photo=urllib .request .urlopen(each )
#     w=photo .read()
#     #打开指定文件，并允许写入二进制数据
#     f=open('./testimg/'+filename,'wb')
#     #写入获取的数据
#     f.write(w)
#     #关闭文件
#     f.close()
#
# #该模块既可以导入到别的模块中使用，另外该模块也可自我执行
# if __name__=='__main__':
#   #定义url
#   # url="http://findicons.com/pack/2787/beautiful_flat_icons"
#   url="https://images.pexels.com/photos/4245825/pexels-photo-4245825.jpeg"
#   #将url作为open_url()的参数，然后将open_url()的返回值作为参数赋给get_img()
#   get_img(open_url(url))
