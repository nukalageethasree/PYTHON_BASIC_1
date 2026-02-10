def find_ch(s,c):
    index=0
    count=0
    while(index< len(s)):
        if s[index]==c:
            print("we found the string at:",index)
            count+=1
        else:
            print("we have'nt found the character in the  string at : ",index)    
        index+=1  
    print("no of character u want in the string",count)      
       

            


s=input("enter the string:")
c=input("enter which character u want to search:")
find_ch(s,c)  
''' modifi  the above code so that it starts counting from the specified location 
def find_ch(s, c, start_index):
    index = start_index
    count = 0
    while index < len(s):
        if s[index] == c:
            print("We found the character at:", index)
            count += 1
        else:
            print("We haven't found the character at:", index)
        index += 1  
    print("Number of times the character appeared:", count)

# Input section
s = input("Enter the string: ")
c = input("Enter the character you want to search for: ")
start_index = int(input("Enter the index to start the search from: "))

# Function call
find_ch(s, c, start_index)
'''  