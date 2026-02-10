print("ENTER -1 TO EXIT THE  CODE")
circumference={}
while True:
    r= float(input("enter radius:"))
    if r==-1:
        break
    else:
        dict={r:2*3.14*r}
        circumference.update(dict)
print(circumference)
        