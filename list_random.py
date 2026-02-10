import random
num_list=[]
for i in range(10):
    val=random.randint(1,100)
    num_list.append(val)
print("original list:",num_list)
even_list=[]
odd_list=[]
for i in range(len(num_list)):
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even number list :",even_list)       
print("even number list :",odd_list)          
