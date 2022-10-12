#  truncate  可以对源文件进行截取操作
fobjB=open('text.txt','r',encoding='utf-8')
print(fobjB.read())
fobjB.close()
print('截取之后的数据')
#   r+ 实现对文件的读取和修改的操作模式
fobjA=open('text.txt','r+',encoding='utf-8')
fobjA.truncate(15)  #截取文件15个字符 在原有文件的基础上进行数据的截取
print(fobjA.read())
fobjA.close()