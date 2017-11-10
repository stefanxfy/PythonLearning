# 字符串拼接
#1.  +
s='hello'
t='python'
r='!'
#print(s+t+r)#hellopython!

#2.格式化输出 %s
#print("%s %s %s"%(s,t,r))#hellopython!

#3.join
c=('hello','python','!')
c=" ".join(c)  #()内必须是可迭代对象
#print(c)#hello python !

#4. format
d='{0} {1} {2} {3}'.format(s,t,r,99)  #传入任意参数
print(d)#hello python ! 99
d='{a} {b} {c}'.format(a=s,b=t,c=r)  # 字典无序
print(d)#hello python !