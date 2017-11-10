# 深浅复制

#浅复制
l1=[0,1,['hello','world']]
l2=l1.copy()  #[0, 1, ['hello', 'world']]
#深复制
import copy
l3=copy.deepcopy(l1) #[0, 1, ['hello', 'world']]
l4=copy.deepcopy(l1[2]) #['hello', 'world']
'''print(id(l1)) #1885657483528
print(id(l2)) #1885657483336
print(id(l3)) #1885657674120'''

'''print(id(l1[2])) #2169172818248
print(id(l2[2])) #2169172818248
print(id(l3[2])) #2169173004040
print(id(l4)) #2169174391880'''

l2[2][0]="hahaha"
'''print(l1)
print(l2)
print(l3)'''
'''
[0, 1, ['hahaha', 'world']]
[0, 1, ['hahaha', 'world']]
[0, 1, ['hello', 'world']]
'''

#总结 浅复制和深复制对整体的内存位置都变了，但是浅复制对于嵌套列表的地址不变，深复制对于嵌套列表的地址变了
#深浅复制只存在于嵌套列表中


