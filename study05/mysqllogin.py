# import sys
# print("参数的个数是",len(sys.argv),"个参数")
# print("参数的值是",str(sys.argv[1:]))

import argparse #导入
#创建一个解释器对象
parser=argparse.ArgumentParser(prog='系统登录',usage='%(prog)s [options] usage',
                              description='系统自定义自命令行的文件',epilog='my-epilog')

#添加必选参数 也叫位置参数
parser.add_argument('loignType',type=str,help='系统登录类型')

#添加可选参数  一个用户名  一个密码
parser.add_argument('-u',dest='user',type=str,help='你的用户名')
parser.add_argument('-p',dest='pwd',type=str,help='你的密码')



result=parser.parse_args()  #开始解析参数

if(result.user=='root' and result.pwd=='111'):
    print("用户登录成功")
    pass
else:
    print("用户登录失败")
    pass



