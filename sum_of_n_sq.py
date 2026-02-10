start=int(input("enter the starting number of sequence:"))
end=int(input("enter the end number : "))
sum=0
for i in range(end):
    result=start**2/2
    sum=sum+result
    start+=1
print(f"sum of the values:{sum}")    

 