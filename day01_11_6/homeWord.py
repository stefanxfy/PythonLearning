#1.定义讲过的每种数值类型，序列类型
#整型 int
a=12
print(type(a))
#浮点型  float
b=1.3
print(type(b) )
#复数
f=1+2j
print(type(f))
#布尔值  bool
c=True
print(type(c))
#字符串
s="12324"
print(type(s))
#列表
l=[1,2,3]
print(type(l))
#元组
t=1,2
t2=(1,)
print(type(t),type(t2))

#2.python里面怎么注释代码？
#用'''   '''多行注释
#  用#单行注释

#3.简述变量的命名规则
#变量命名的规则(用help()查看关键字)：
# 不能是Python的关键字
# 不能以数字开头
# 变量名的组成只能是字母数字下划线（_）组成

#4.长度为5的列表 li=['a','b','c','d','e']，至少用4种方法，取第3位的值

li=['a','b','c','d','e']
print(li[2])
print(li[2:3])
print(li[-3])
print(li[2:1:-1])

#5.有个时间形式是（20171107），通过除法和取余，来得到对应的日，月，年。请用代码完成。
date=20171107
y=date//10000
m=date%20170000//100
d=date%2017110
print("%d年%d月%d日"%(y,m,d))