string=input("enter the string:")
sentance=string.lower()
count=0
for i in range(len(sentance)):
    vowels="aeiou"
    if sentance[i] in vowels:
        count+=1
print("number of vowels:",count)
conc=len(sentance)-count
print("number of conconents",conc)        
