'''message=input("enter the string")
vowels="aeiouAEIOU"
result=""
for char in message :
    if char not in vowels:
        result+=char
    
print(result) ''' 
message=input("enter the string ")
index=0
result=0
while index<len(message):
    vowels="aeoiuAEIOU"
    if message[index] not in vowels :
        print(message[index])
    index+=1   