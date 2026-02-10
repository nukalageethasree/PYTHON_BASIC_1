numbers=list(map(int,input("enter number seperated by space:").split()))
a=len(numbers)-1
b=[]
print("the original list",numbers)
while a>=0:
    b.append(numbers[a])
    a-=1
print("the reserved list",b)    