import random
import threading
import urllib.request  # 导入用于打开URL的扩展库模块
import urllib.parse
import re  # 导入正则表达式模块


class DownLoadImg(threading.Thread):
    def __init__(self,  packName, num):
        self.packName = packName
        self.num = num
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.num):
            print(self.packName+"--"+str(i))
            name = str(int(10000000 * random.random()))
            url = "https://images.pexels.com/photos/" + name + "/pexels-photo-" + name + ".jpeg"
            req = urllib.request.Request(url)  # 将Request类实例化并传入url为初始值，然后赋值给req
            # 添加header，伪装成浏览器
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
            # 访问url，并将页面的二进制数据赋值给page
            try:
                page = urllib.request.urlopen(req)
                # 将page中的内容转换为utf-8编码
                html = page.read()  # .decode('utf-8')
                f = open('G:/Python爬取的图片/' + self.packName + '/' + name + '.jpeg', 'wb')
                # 写入获取的数据
                f.write(html)
                # 关闭文件
                f.close()
                print(name)
            except:
                print("no" + name)
                pass

# 该模块既可以导入到别的模块中使用，另外该模块也可自我执行
if __name__ == '__main__':
    down=DownLoadImg("pexels19",1000)
    down1=DownLoadImg("pexels20",1000)
    down.start()
    down1.start()


