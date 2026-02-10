def f(a,b):
  a,b = b,a
  print("after swap")
  print("a value after swap",a)
  print("b value after swap",b)
a=(input("enter the value of a:"))
b=(input("enter the value of b:"))  
f(a,b)
