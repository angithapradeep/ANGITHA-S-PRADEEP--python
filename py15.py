#to find distance between two points
#it is found out using equation =>  d=√((x2 – x1)² + (y2 – y1)²).
import math
print("enter the points :")
x1=int(input("enter the x coordinate of the first point :"))
y1=int(input("enter the y coordinate of the first point :"))
x2=int(input("enter the x coordinate of the second point :"))
y2=int(input("enter the y coordinate of the second point :"))
d1=(x2-x1)**2
d2=(y2-y1)**2
d=math.sqrt(d1+d2)
print(d)
