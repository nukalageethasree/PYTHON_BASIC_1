def square(x):
    return x**2
inp_list=input("enter the string values:")
imp_list=list(map(int,inp_list.split( )))
print("given list:",imp_list)
square_list=list(map(square,imp_list))
print("square of the given list",square_list)
sum=0
for i in square_list:
    sum+=i
print("sum of squares in the range ",sum)    