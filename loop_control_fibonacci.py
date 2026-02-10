n = int(input("enter the number till you want the series: "))
a = 0
b = 1

while a <= n:
    print(a)
    
    temp = a + b   # calculate next number
    a = b          # shift values
    b = temp
 