s1=input("enter the string:")
unique=True
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        if s1[i]==s1[j]:
            unique=False
            
if unique==True:
    print("the string  is unique string ")
else:
    print("the string did'nt have unique string")    