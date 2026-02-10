a=0
b=1
n=int(input("enter the n value:"))
print(a)
print(b)
c=a+b
print(c)
while c<=n :
   a=b
   b=c
   c=a+b
   if c<n:
    print(c)
