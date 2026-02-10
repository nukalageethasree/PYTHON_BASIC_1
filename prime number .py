number=int(input("enter the number"))
count=0
if number==2:
  print("the given number is prime number ")
elif number==1:
  print("the given number is nor prime nad composite") 
else:  
 for i in range(2,number+1):
   if number%i==0:
     count=count+1
if (count==1):
  print("the given number is prime number ")     
else:
  print("the given number is the composite number ")