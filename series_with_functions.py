def fun(n):
    f=1
    total=0
    if n==0 :
        return 1
    else:
        for i in range(1,n+1):
            f=f*i
            ans=i**i/f
            total=total+ans
        return total
n=int(input("enter the value of n:"))
print(fun(n))