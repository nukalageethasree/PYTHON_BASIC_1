string=input("enter the string:")
rev_str=""
i=len(string)-1
while i>=0:
    letter=string[i]
    rev_str=rev_str+letter
    i-=1
print("the reverse string is:",rev_str)    
