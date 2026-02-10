string = input("Enter the string: ")
vowel = "aeiou"
sentance = string.lower()
result = ''

for i in range(len(sentance)):
    if sentance[i] in vowel:
        continue
    else:
        result = result + sentance[i]

print(result)

