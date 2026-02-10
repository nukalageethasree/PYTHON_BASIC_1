sentence=input("enter the sentence:")
result=""
space=" "
for chr in sentence:
    if chr==space:
        continue
    else:
        result+=chr
print(result)