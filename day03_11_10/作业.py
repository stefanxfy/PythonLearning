#print("hello",'python','hahaha',sep=',')#   hello,python,hahaha  sep默认是' '
#print('hello',end="---")# 默认 end='/n'

l=[1,2,3]
print('{0[0]},{0[1]},{0[2]}'.format(l))# 1,2,3

print('',12,'',sep='****')
print('{:*^10}'.format(12))  # :后面第一位是填充字符，第二个^是居中，第三个是占多少位
print('{:*<10}'.format(12))  #<  左对齐