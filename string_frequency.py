string = input("Enter the string: ")
n = len(string)
i = 0

while i < n:
    count = 1
    j = i + 1
    while j < n:
        if string[i] == string[j]:
            count += 1
        j += 1
    # Only print if the character didn't appear before
    if string[i] not in string[:i]:
        print(f"The frequency of '{string[i]}' character in the string is {count}")
    i += 1
