#len()
#max()# 迭代参数
#min()# 迭代参数
l=[1,2,3,4,45,5]

l.sort()# [1, 2, 3, 4, 5, 45]
#print(l)
#print(sorted(l))#[1, 2, 3, 4, 5, 45]
l.reverse()

#print(l)# [45, 5, 4, 3, 2, 1]
#print(list(reversed(l)))# [1, 2, 3, 4, 5, 45]

#print(sum([1,2,3]))#6

#enumerate 枚举
#print(list(enumerate(l)))# [(0, 45), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
'''for index,value in enumerate(l):
    print(index,value)'''
'''
0 45
1 5
2 4
3 3
4 2
5 1
'''

#filter 过滤
g=lambda x :x>3
f=filter(g,l) #g位函数，l为可迭代对象
# print(list(f))# [45, 5, 4]

#map
def m(x):
    return x**2
m=map(m,l) #m位函数，l为可迭代对象
#print(list(m))# [2025, 25, 16, 9, 4, 1]

#zip
s="hello"
t=(1,2,3,4)
tt=('2','3','45','78')
z=zip(s,t,tt)   #填写很多个迭代参数
#print(list(z))# [('h', 1, '2'), ('e', 2, '3'), ('l', 3, '45'), ('l', 4, '78')]

#进制转换函数
b=bin(4)# 二进制0b100
a=oct(10)#八进制0o12
h=hex(17)# 十六进制0x11
o1=ord('a')#97
o2=ord('A')#65
c=chr(97)# a
#print(b,a,h,o1,o2,c)