def reverse(str):
    new_str=""
    i=len(str)-1
    while i>=0:
        new_str+=str[i]
        
        i-=1
    print("reverse the string:",new_str)    
str=input("enter the string:")
reverse(str)        
        