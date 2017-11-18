'''i=2
zhishu=[]
while(i<=100):
    for j in range(2,i-1):
        if i%j==0:
            print("%d不是质数"%i)
            break
    else:
        print("%d是质数"%i)
        zhishu.append(i)
    i+=1
print(zhishu)
'''
#  a,b交换
a=1
b=2
a,b=b,a
print("a:%s,b:%s"%(a,b))
