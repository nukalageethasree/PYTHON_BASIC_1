def circulate(L, n):
    print("Circulating the elements of list")
    for i in range(n):
        val = L.pop(0)   # remove first element and get its value
        L.append(val)    # put that value at the end (rotates left by 1)
        print(L)

n = int(input("Enter number of values: "))
L = []
for i in range(n):
    val = int(input("Enter a value: "))
    L.append(val)

circulate(L, n)
      

 