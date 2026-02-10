string=input("enter the string:")
result=''
for i in string:
    if i not in result:
        result+=i
print("string with out duplicates",result)        