# 2(a+b)=2a+2b+2ab
#if lhs=rhs then true else false
a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
lhs=2*(a+b)
rhs=(2*a)+(2*b)+(2*a*b)
if lhs==rhs:
    print("true")
else:
    print("false")
