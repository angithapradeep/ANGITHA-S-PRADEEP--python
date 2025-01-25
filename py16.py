#roots of quadratic equation
import math
b=int(input("enter the value of b :"))
c=int(input("enter the value of c :"))
a=int(input("enter the value of a :"))
r1=type(float)
r2=type(float)
s=((b*b)-4*a*c)
if s>0:
    b1=math.sqrt(s)
    r1=((-b)+b1)//2*a
    r2=(b-b1)//2*a
    print("r1 =",f"{r1:.3f}")
    print("r2 =",f"{r2:.3f}")
elif s==0:
    r1 = -b/(2*a)
    print("r1 =",r1)
    print("Both roots are equal")
else:
    print("roots are complex!!!!!!!!!!")
