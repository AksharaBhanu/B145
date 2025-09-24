# a=100
# result=type(a)
# print(result)

a=100
#we are calling 2 functions
#outer function is print
#inner function is type
#inner function will execute 1st and then the outer function
print(type(a))
#first it will execute 'type' it will find the data type of 'a' -> int
#it returs int to outer function (print)
#print will take 'int' as input and prints it on the console