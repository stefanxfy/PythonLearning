'''
参数的定义顺序：必备参数(位置)，默认参数，不定长参数，关键字参数

'''
def fun(x,y=2,*arg,**kwarg):  #*arg 以元组的形式传入函数，**kwarg以字典形式
    print(x)
    print(y)
    print(*arg)
    print(arg)
    print(kwarg)
    print(*kwarg)
#*作用：拆包    字典--》键值对
    #*arg    0-任意多个 任意参数
    #**kwarg   0-任意多个  任意多个含有参数名的

#默认参数不能放到必备参数前面
#*arg在前时，默认参数可以放到必备参数前

def fun1(*arg,x,y=2):
    print(x)
    print(y)
    print(*arg)
    return '运行完了'
    print('真的吗')
    
g = lambda x:x+1

### 几个常用的内置函数
dir(__builtins__)
a=dict(a=1,b=2,c=3,d=4)
len(a)

sorted
reversed
li = [11,33,22,99,66]
li.sort()
new=sorted(li)

sum
sum([1,3,5])
sum([1,3,5],10)


enumerate
#枚举

##for i in li:
##    print(li.index(i),i)
##
##for k,v in enumerate(li):
##    print(k,v)
##for ii in enumerate(li):  
##    print(ii)
##
##
##list(enumerate(li))
##list(enumerate(li,10))
##
##
##filter
##
##
##gg = lambda x:x>4
##
##def ggg(x):
##    return x>4
##
##l1=[1,9,3,6,66,99,88]

map

def mm(x):
    return x**2
l2=[1,2,3,4,5]
list(map(mm,l2))


zip    #zip(iter1 [,iter2 [...]]) --> zip object
s='hello'
t=(1,2,3,4,5)
tt=(1,2,3,4,5,6,9,7)
list(zip(s,t))
list(zip(s,t,tt))

bin(3)  # '0b11'   二进制前缀 0b
oct(9)  # '0o11'
hex(17) # '0x11'

ord('a')
ord('A')
chr(65)
chr(97)

#作用域
a = 110  #全局作用域

def f1():     #函数内部不能直接修改外部变量
    print(a)
    a = a+1
    return a+1

def f2():   
    a=0          #局部作用域
    print(a)
    a = a+1
    return a+1


def f3():
    global a   #能够修改外部的变量  (函数内与外)
    print(a)
    a = a+1
    return a+1
b=c=0
def f4():
    global b
    b=998
    print(b)
    global c
    c=666
    print(c)
    return b,c

def f5(x):        #函数的嵌套
    x += 1
    def ff5(y):
        return x*y
    return ff5
    
a=110    # 全局作用域   global
def f6():
    a = 10   #  闭包函数外的函数中  enclosing
    def ff6():
##        global a   # a=110
        nonlocal a   # a=10
        a += 1      # 局部作用域 local
        print(a)
        return a+1
    return ff6()


def f7():  # 写了就被开除   不能瞎用全局变量
    global a
    a += 1
    return a

#装饰器，  面向对象才会讲

#1.高阶函数   2.闭包   3.函数即变量

#高阶函数: 可以接受函数作为参数，或者返回值是函数

def f8():
    print('我要做高阶函数的参数')

def f9(func):
    func()
    func()
    return func()
##f9(f8)

def f5(x):        #函数的嵌套  闭包
    x += 1
    def ff5(y):
        return x*y
    return ff5
##f5(5)
##f5(5)(10)

###递归函数   
#阶乘    8！=1*2*3*4*5*6*7*8   n!=1*2*3....*n  1!=1

def f(n):
    if n == 1:
        return 1
    return f(n-1)*n   #f(5)= f(4)*5  f(3)*4*5  f(2)*3*4*5 1*2*3*4*5
                            #f(4)=f(3)*4  f(3)=f(2)*3 f(2)=f(1)*2

f(3)
f(4)
