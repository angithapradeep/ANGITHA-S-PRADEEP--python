#to find a perfect number(a positive integer that is equal to 
# the sum of its positive proper divisors, excluding the number itself)
n=int(input("enter the number :"))
num=n
sum=1
rem=0
for i in range (2,n):
    if n%i==0:
        rem=n//i
        sum=sum+i
if sum==num:
    print('perfect number')
else:
    print("not a perfect number")
