a=0
b=1
n=int(input("enter the number of terms:"))
i=2
list=[a,b]
while i<n :
    s=a+b
    list.append(s)
    a=b
    b=s
    i+=1
print(list)
i=0
sum=0
while i<n:
    sum+=list[i]
    i+=2
print("sum=",sum)        