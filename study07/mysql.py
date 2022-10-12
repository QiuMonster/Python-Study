# import pymysql  #导入数据库模块
from pymysql import *

# 创建数据库连接
conn = connect(host='localhost', user='root', password='qq1773326851',
               database='bookdb', port=3306, charset='utf8')


def foreach(res):
    for i in res:
        print("地址编号：{},用户姓名：{},地址详情：{},电话：{},用户编号：{}".format(i[0], i[1], i[2], i[3], i[4]))
        print()
        pass


# 创建一个游标对象  可以通过这个游标进行数据库操作
try:
    cur = conn.cursor()

    # 查询sql
    # cur.execute("select * from tb_address where uid='u001'") #执行sql语句  添加参数
    # res=cur.fetchall()  #获取游标中查询到的所有值
    # foreach(res)

    # 参数查询sql
    # selectsql="select * from tb_address where uid=%s;"  # %s表示是一个参数
    # val=['u001']; #参数类型是一个列表
    # cur.execute(selectsql,val)
    # print(cur.fetchall())

    # 进行插入操作
    # insertsql = "insert into tb_address(name,detail,phone,uid) values('qiu','南京使','110','u003')"  # 插入数据的sql
    # res = cur.execute(insertsql)
    # print(res)  # 查看数据库受影响行数
    # conn.commit()  # 进行数据的提交操作

    # 进行删除操作
    # deletesql="delete from tb_address where no=%s "
    # val=[12]
    # res=cur.execute(deletesql,val)
    # conn.commit() #除了查询不提交 其他的都要提交
    # if res==1:
    #     print("删除成功")
    #     pass
    # else:
    #     print("删除失败")

    # 进行更新操作
    # updatesql = "update tb_address set name=%s,detail=%s,phone=%s where no=%s "
    # val = ['lks', '别境路', '123456789',12]
    # res = cur.execute(updatesql, val)
    # conn.commit()
    # if res == 1:
    #     print("更新成功")
    #     pass
    # else:
    #     print("更新失败")

except Exception as msg:
   print(msg.args)
   pass
finally:
   cur.close()  # 关闭游标
   conn.close()  # 关闭连接
