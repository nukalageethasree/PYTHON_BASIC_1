number=int(input("enter the number:"))
b=len(str(number))
temp=number
sum=0
while number>0:
    number1=number%10
    
    number2=number1**b
    sum=sum+number2
    number=number // 10
if sum==temp:
    print("the given number is amstrong number",sum)
else:
    print(" the given number is not a amstrong number")
        

