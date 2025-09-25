#i want to create read only list
list1=[10,20,30]
print(type(list1)) #list
print(list1)
print(list1[0])

list1[0]=15
print(list1)


t1=(10,20,30)
print(type(t1)) #tuple--read only list
print(t1)
print(t1[0])
t1[0]=15
print(t1)