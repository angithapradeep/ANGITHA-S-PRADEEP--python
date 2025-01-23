#check if triangle is right triangle
s1=int(input("enter  side1:"))
s2=int(input("enter side2 :"))
s3=int(input("enter side3:"))
large=0
small1=0
small2=0
if s1>s2 and s1>s3:
    large=s1
    small1=s2
    small2=s3
elif s2>s1 and s2>s3:
    large=s2
    small1=s1
    small2=s3
else:
    large=s3
    small1=s2
    small2=s1
if large**2 == (small1**2)+(small2**2) :
    print("right triangle")
else:
    print("not right triangle")