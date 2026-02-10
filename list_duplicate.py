'''list_1=[1,2,3,6,4,7,1,9,6]
i=0
while i<len(list_1):
    num =list_1[i]
    j=i+1
    while j < len(list_1): 
        
        if list_1[j]==num:
            list_1.pop(j)
        else:
            j+=1
    i+=1
print("after removing the duplicates",list_1) ''' 
numbers=list(map(int,input("enter the numbers:").split()))
b=[]
for num in range(len(numbers)):
    for num2 in range(num+1,len(numbers)):
        if numbers[num]==numbers[num2]:  
            break
    else:
        b.append(numbers[num])
print("after removing all the duplicates from the list",b)                        

