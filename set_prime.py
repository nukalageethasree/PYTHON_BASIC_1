odds=set([x*2+1 for x in range(1,10)])
print(odds)
primes=set()
for i in range(2,20):
    j=2
    while j<i//2:
      if  i%j==0:
         
         j+=1
      else:
          primes.add(i)
          j+=1
print(primes)
print("union:",odds.union(primes))
print("intersection:",odds.intersection(primes))
print("symmetric difference:",odds.symmetric_difference(primes))
print("difference:",odds.difference(primes))



         
