num=int(input("enter a number"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("the number is a pallindrome") 
else:
    print("the number is not a pallindrome")       