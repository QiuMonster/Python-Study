# import sys
# print("参数的个数是",len(sys.argv),"个参数")
# print("参数的值是",str(sys.argv[1:]))

import argparse #导入
#创建一个解释器对象
parser=argparse.ArgumentParser(prog='我自己的程序',usage='%(prog)s [options] usage',
                              description='编写自命令行的文件',epilog='my-epilog')

#添加必选参数 也叫位置参数
parser.add_argument('name',type=str,help='你自己的名字') #添加参数
parser.add_argument('age',type=str,help='你自己的年龄')

#添加可选参数
#1   -s是可选标识  action='append'表明后面可以添加多个值  是一个列表属性
# parser.add_argument('-s','--sex',action='append',type=str,help='你的性别')

#限定范围  choices=[]
parser.add_argument('-s','--sex',default='男',choices=['男','女','male','fmale'],type=str,help='你的性别')

# print(parser.print_help())  #输出信息

result=parser.parse_args()  #开始解析参数

print(result.name) #直接输出元组中的参数值


