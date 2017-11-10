#格式化输出
# %s 字符串
a='%s,%s' %('hello','world') #%s 可以输字符串，数字
print(a)#hello,world
 # %d 数字
#b='%d,%d'%("he",'hei')#  %d 只能输数字 TypeError: %d format: a number is required, not str
#print(b)

 # %r
#print(str(123))# 123
#print(repr('123'))#'123'
#print(repr(123))#123

#%f  浮点
#print('%f'%(12))#12.000000
#print("%.2f"%(12))# 12.00
#print("%8.2f"%(12))#   12.00
#小数点后是控制精确度，小数点前是控制整个长度，小数点后的数字总是起效的
#print("%+-6.2f"%(12))#+12.00
#print("%09.2f"%(12))#000012.00

#科学计数法  %e
'''print("%e"%1) #1.000000e+00 1*10 0次
print("%e"%10) #1.000000e+01 1*10 1次
print("%e"%100) #1.000000e+02 1*10 2次
print("%e"%1.3)#1.300000e+00 1.3* 10 0次'''

#  %x %o
#print("%x"%15)# f  16进制
#print("%o"%9) #11 8进制

# \n 换行 \a  \b \t
#print("hhhh\ndddd")
#print("hh\bddd") #hddd
#print("hh\tddd") #hh	ddd
# %c
print("%c"%97)# a  对应输出ASCII的值
