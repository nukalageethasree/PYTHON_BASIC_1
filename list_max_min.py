numbers=list(map(int,input("enter number seperated by space:").split( )))
maximum=numbers[0]
minimum=numbers[0]
for num in numbers:
    if num > maximum:
        maximun=num
    if num<minimum:
        minimum=num
print("list",numbers)
print("maximum number in the list",maximum)
print("minimum number in the list",minimum)            