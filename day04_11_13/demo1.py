#集合set 无序，唯一性
#定义集合
ss=set()
l=[1,23,4,45,65,77]
s1=set(l)
#print(s)# {65, 1, 4, 45, 77, 23}
s2={1,3,2}
s3={1,2,4}
#交集
'''print(s2.intersection(s3))#{1, 2}
print(s2&s3) #{1, 2}'''
#并集
'''print(s2.union(s3))#{1, 2, 3, 4}
print(s2|s3) #{1, 2, 3, 4}'''

#差集
'''print(s2-s3) #{3}
print(s3-s2) #{4}
print(s2.difference(s3))#{3}
# ^ s2，s3先合并，再去除两个集合都有的
print(s2^s3) #{3, 4}
'''
# add update remove clear
'''s3={2,1,4,55}
s3.add(34) #只添加一个
s3.update((15,36,46)#添加多个 参数为迭代器iterable
print(s3)
#s3.remove(3)
#s3.clear()'''
