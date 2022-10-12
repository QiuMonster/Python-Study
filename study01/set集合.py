#定义一个set集合  特点是不允许重复
setA={1,2,3,4,4,4}
print(setA)

# setA.add('qwqw')
print(setA)  #可以添加字符串类型
# setA.clear()  #将set中集合删除
print(setA)
setB={1,2,4,5,7}
#差集操作
print(setA.difference(setB))  #setA-setB  A中存在B中不存在的元素
#并集操作
print(setA.intersection(setB))  #使用元素之间的并集操作
#集合操作
print(setA.union(setB))  #元素的集合操作  其实就是并集操作
print(setA|setB)  #第二中并集操作  与union效果相同
#从集合中取数据
print(setA.pop())  #pop函数取出的是最外侧的数值
#这个类似于出栈   setA中的元素会去掉这个元素
print(setA)
#指定移除set中的数据
setA.discard(2)  #移除set中的第二个元素   元素的排列是不变化的固定位置 删除一个元素 其他元素也不会向前移动
print("移除指定元素",setA)
#更新集合操作  update()
setA.update({7,8,9})  #其实是添加数据操作
print(setA)