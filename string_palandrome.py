'''string=input("enter the string:")
i=0
j=len(string)-1
is_palandrome=True
while i<j:
    if string[i]!=string[j]:
        is_palandrome=False
        print("not a plandrome ")
        break
    i+=1
    j-=1
    if is_palandrome:
        print("yes")
    else:
        print("no") '''
s = input("Enter the string: ")
start = 0
end = len(s) - 1

while start < end:
    if s[start] != s[end]:
        print("The given string is not a palindrome")
        break
    start += 1
    end -= 1
else:
    print("The given string is a palindrome")


