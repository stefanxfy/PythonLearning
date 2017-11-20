#作用域
a=11
def f1():
    #a=0 #  2
    global a  # 13
    a=a+1
    return a+1
#print(f1())# 2

#函数嵌套
def f2(x):
    x+=1
    def f3(y):
        return x+y
    return f3
#print(f2(10)(3)) #14

a=110
def f4():
    a=10
    def f5():
       # global a #使用函数外参数
        nonlocal a  #使用函数内部参数
        print(a) #10
        return a+1 #11
    return f5()
#print(f4())


##高阶函数 参数为函数
def f7():
    print("我哈哈哈")
def f8(f7):
    f7()
    f7()
#f8(f7) #我哈哈哈
        #我哈哈哈


##闭包函数 返回内嵌函数

def f9(x):
    x+=1
    def f10(y):
        return x+y
    return f10
#print(f9(10)(8))

#递归函数
def fun(n):
    if n==1:
        return 1
    return fun(n-1)*n
'''
n=3
fun(3)
fun(2)*3
fun(1)*2
fun(1)*fun(2)*fun(3)

'''