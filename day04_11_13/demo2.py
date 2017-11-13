### 字典
d={'12':123,'34':543}
### list 和dict 的取值速度
##dict更快
##############################################
######dict的方法
#d.clear()
#d.copy()

#print(d.fromkeys((1,2,3),666)) #{1: 666, 2: 666, 3: 666}

d.get(23)  #不存在返回None
a=d.items()
#print(list(a)) #[('12', 123), ('34', 543)]
#d.keys()
#d.values()

#pop
#print(d.pop('12'))# 移除'12'，返回移除的value
#print(d.pop('1233',2324)) # 不存在，返回2324
d={'12':123,'34':543,'54':666}

#popitem
#print(d.popitem()) #('54', 666) 随机删除一个键值对
#{}.popitem() #KeyError:
d.setdefault('hah','lala')
#print(d) #{'12': 123, '34': 543, '54': 666, 'hah': 'lala'}
d.setdefault('12','hah')
#  执行过程：如果键存在，返回值，如果不存在，创建
d.update({'jj':'dd','gg':'bb'})
print(d)#{'12': 123, '34': 543, '54': 666, 'hah': 'lala', 'jj': 'dd', 'gg': 'bb'}
