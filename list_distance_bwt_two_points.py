import math
p1=[]
p2=[]
x1=int(input("enter the x cordinate of starting point :"))
y1=int(input("enter the y cordinate of starting point :"))
x2=int(input("enter the x cordinate of ending point :"))
y2=int(input("enter the y cordinate of ending point :"))
p1.append(x1)
p1.append(y1)
p2.append(x2)
p2.append(y2)
distance=math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print("distance=%f"%distance)