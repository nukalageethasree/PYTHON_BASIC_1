numbers=[2,9,4,20,16,5,4,5]
for num in range(0,len(numbers)):
    count=1
    for number2 in range(num+1,len(numbers)):
        if numbers[num]==numbers[number2]:
            count+=1
    print(f"the number of {numbers[num]}:",count)