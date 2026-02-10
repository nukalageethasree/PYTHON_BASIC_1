number=int(input("enter the number :"))

if number ==2:
    print("the given number is a prime number ")
elif number==1:
    print("the given number nor composite nor prime  number")    
else:
    for i in range(2,int(number**0.5+1)):
        if(number%i!=0):
            print("the given number is prime number")
        else: 
            print("the given number is composite number ")