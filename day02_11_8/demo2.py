#字符串方法
a='helloworldhello'
#print(a.count("hello")) #统计元素出现的次数2
a.index('l')#返回索引
a.find('l') #和index很像，但是find找不到元素返回-1，不会报错

#####头尾判断
a.endswith('hello') #以o结尾返回True
a.startswith("hello")

#####元素类型判断
a.isalpha() #判断字符串内是否为字母
a.isdigit()#判断字符串内是否为数字
a.isalnum() #判断字符串内是否为数字or/and字母
a.isupper()
a.islower()


######替换replace
b="zzzzssssdklsdk"
b1=b.replace('z','Z')#全部替换
b1=b.replace('z','Z',3)#第三个参数为替换次数
print(b1)

#######切割 split
c="aaa1sss1sads1dsd"
lc=c.split("1",2) #第一个参数为切除的部分，第二个参数为切几次,返回list


######join 拼接
a="hello"
aa='@'.join(a) # h@e@l@l@o .前面只能是一个字符串，括号里可以填可迭代对象
b=["1","2",'3']
aaa=aa.join(b) ##但是元素只能都是字符串，不然不能拼接
print(aaa)