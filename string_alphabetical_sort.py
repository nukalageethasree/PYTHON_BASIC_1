'''sentence=input("enter the string:")

sorted=sorted(sentence)
result=(''.join(sorted))
print("the sorted value of the sentance in alphabetical order",result)'''
sentence = input("Enter the string: ")

words = sentence.split()            
words_sorted = sorted(words)        
result = ' '.join(words_sorted)     

print("The sorted value of the sentence in alphabetical order:", result)
