inp_list=input("enter the value of the list")
num_list=list(map(int,inp_list.split( )))
num1=int(input("enter the value of num"))
i=0
count=0
while i<len(num_list):
    if num1==num_list[i]:
        print("num1 is equal to num_list[i] at index:",i)
        count+=1
    i+=1
print("total number of num1 match",count)
    


