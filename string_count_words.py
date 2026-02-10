'''sentence=input("enter a sentance:")
words=sentence.split( )
for word in words:
    print(f"no of {word}is given sentence",words.count(word))'''
sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""

for i in range(len(words)):
    count = 1
    for j in range(i+1, len(words)):
        if words[i] == words[j]:
            count += 1
    # avoid duplicates by checking result string
    if f"'{words[i]}'" not in result:
        result += f"No of '{words[i]}' in given sentence: {count}\n"

print(result)
