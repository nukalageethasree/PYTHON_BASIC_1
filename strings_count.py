string=input("enter the string")
count1=0
count2=0
count3=0
count4=0
for i in string:
    if string.isalpha():
        count1+=1
    elif string.isspace():
        count2+=1
    elif string.isdigit():
        count3+=1
    else:
        count4+=1
print("number of alphabets",count1) 
print("number of space",count2)
print("number of digits",count3)
print("number of special characters",count4)               
        