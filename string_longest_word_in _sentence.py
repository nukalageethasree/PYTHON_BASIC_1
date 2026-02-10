sentence=input("enter a sentence:")
words=sentence.split()
result=""
for word in words:
    if len(word)>len(result):
        result=word
print("the longest word in the sentance",result)        

