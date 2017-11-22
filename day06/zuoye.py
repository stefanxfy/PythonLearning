

#2
def fun(li):
    return sorted(li)
li= [9, 8, 3, 2, 6, 4, 5, 7, 1]
#print(fun(li))


#冒泡排序
li= [9, 8, 3, 2, 6, 4, 5, 7, 1]
def maopao(seq):
    for j in range(len(li)):
        for i in range(len(li)-1):
            if seq[i]>seq[i+1]:
                seq[i],seq[i+1]=seq[i+1],seq[i]
    print(seq)
#maopao(li) ##[1, 2, 3, 4, 5, 6, 7, 8, 9]

l2=[(13,23,3),(4,5,6),(8,9,6)]
#需求以元组第二个数字进行排序
l2.sort(key=lambda x :x[1])
print(l2)
print(sorted(l2,key=lambda x :x[1]))
