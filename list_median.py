list=[]
n=int(input("enter the number of elements to be inserted  in the list:"))

for i in range(n):
    print("enter number",i+1,":")
    num=int(input())
    list.append(num)
print("original list",list)    
print("sorted list is .....")
list.sort()
print("sorted list",list)
i=len(list)-1
if n%2!=0: 
    print("median=",list[i//2])
else:
    print("median=",(list[i//2]+list[i+1//2])/2)       

