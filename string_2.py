def copy(str):
    new_str=" "
    for i in range(len(str)):
        new_str+=str[i]
    return new_str
str=input("enter a string:")
print("the new string is:",copy(str))   
 
    