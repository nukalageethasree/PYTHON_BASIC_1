evens=set([x*2 for x in range(1,10)])
print(evens)
composites=set()
for i in range(2,20):
    j=2
    while j<i//2:
        if i%j==0:
            composites.add(i)
        j+=1
print("composites:",composites)
print("evens:",evens.issuperset(composites))
print("all:",all(evens))
print("length of the composite set:",len(composites))
print("sum of all numbers in even set:",sum(evens))

          
