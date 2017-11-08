#列表方法
li=[1,2,3]
li.append(4)
li.clear()
l2=li.copy()
#li.count(1)
#li.index(1)
#extend
li.extend("123")# ['1', '2', '3'] 参数为可迭代对象
#print(li)

#insert
li.insert(2,"5")  #想插到哪个位置，写哪个索引
#print(li)

#pop
li.pop() #删除最后一个
li.pop(1) #删除对应索引的元素

#remove
li.remove("5") #移除指定参数（第一次出现的）

#reverse 翻转
li.reverse()


#sort
l1=[1,3,2,5,6,9,7,4]
li.sort()#默认是从小到大
l1.sort(reverse=False)#TRUE 从小到大，false 从大到小
#print(l1)
l3=['wew','we','fdfg']
l3.sort(key=len,reverse=True) #key=可以是内置方法名，也可是自定义方法名
#print(l3)













