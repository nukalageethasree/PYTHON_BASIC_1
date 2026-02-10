'''message= input("enter the string:")
for i in range(len(message)):
    message_2=chr(ord(message[i])+3)
    print(message_2,end=" ")'''
message= input("enter the string:")
index=0
while index< len(message):
    letter=message[index]
    message_2=chr(ord(letter)+3)
    print(message_2 , end=" ")
    index+=1
    
