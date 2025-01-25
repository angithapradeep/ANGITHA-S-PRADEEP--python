#sum of odd numbers between the limits
lb=int(input("enter the lower limit :"))
ub=int(input("enter th upper limit :"))
sum=0
print("the odd numbers between the limits are :")
if lb%2==0:
    for i in range (lb+1,ub+1,2):
        sum+=i
        print(i,end=",")
else:
    for i in range (lb,ub+1,2):
        sum+=i
        print(i)
print("\nsum of odd numbers is :",sum )
