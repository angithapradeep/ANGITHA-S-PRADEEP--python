# 1/1! + 2/2! + 3/3! + .....n/n!

n=int(input("enter the number of terms :"))
fact=1
sum=0
for i in range(1,n+1):
    fact*=i
    sum=sum+(i/fact)
print("sum of the terms is ",sum)