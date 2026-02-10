def f():
    if(a>b):
        return 1
    elif(b>a):
        return -1
    else:
        return 0
a=int(input("enter the value of a:"))    
b=int(input("enter the value of b:"))
res=f()
if(res==0):
    print("a is equal to b")
elif(res==1):
    print("a is greater than b:")  
else:
    print("b is greater than a")      