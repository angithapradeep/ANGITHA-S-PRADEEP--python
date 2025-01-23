#program to find the power pow(x,y) without using standard function
a=int(input("enter the base value :"))
b=int(input("enter the power value :"))
sum=1
for i in range(1,b+1):
    sum*=a
print("value is",sum)
