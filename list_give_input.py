num_list=[]
m=int(input("enter  the starting of the range:"))
n=int(input("enter  the ending of the range:"))
o=int(input("enter  the step in range :"))
for i in range(m,n,o):
    num_list.append(i)
print("original list:",num_list)
num_list.reverse()  
print("reversed list:",num_list)  

