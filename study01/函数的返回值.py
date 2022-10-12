def Sum(a,b):
    sum=a+b;
    return (sum,12)  #可以返回一个元组  也可以返回一个列表

def GetDict(): #返回一个字典
    return {'name':'qiu'}

print(GetDict())

a=Sum(19,11)
print(a)