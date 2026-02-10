numbers=list(map(int,input("enter the numbers :").split()))

for j in range(len(numbers)):
    for i in range(len(numbers)-1-j):
        if numbers[i]>numbers[i+1]:
            numbers[i] ,numbers[i+1]=numbers[i+1],numbers[i]
print("sorted list",numbers)
print("second largest element",numbers[len(numbers)-2])
print("second smallest element :",numbers[1])