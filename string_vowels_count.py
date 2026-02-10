string=input("enter yhe string:").lower()
vowels="aeiou"
count=0
count1=0
if vowels in string:
    count+=1
else:
    count1+=1
print("no of vowels are:",count)
print("no of consonents are",count1)        
