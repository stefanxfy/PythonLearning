#传递多个参数
def fun(*args):
    print(*args)#1 2 3 4 5 解包
    print(args) # (1, 2, 3, 4, 5) 元组
    print(type(args)) #<class 'tuple'>
#fun(1,2,3,4,5)
t=a,b,c=1,2,3
#print(type(t))# (1, 2, 3)
t=1,2,3 #元组的定义
#print(type(t))

# 关键字参数 **kwarg
def fun1(**kwargs):
    print(kwargs)
#fun1(a=1,b='2') #{'a': 1, 'b': '2'}
#print(dict(a=1,b=4))# {'a': 1, 'b': 4}  字典定义

#  匿名函数
ni=lambda x:x**2
# print(ni(2)) #4

print((lambda x:x%2==0)(4))# True

