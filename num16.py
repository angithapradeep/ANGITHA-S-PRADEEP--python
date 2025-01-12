#program to check whether a 3-digit number is armstrong or not
n=int(input("enter the 3 digit number :"))
num=n
sum=0
rem=0
while n>0:
    rem=n%10
    sum=sum+(rem*rem*rem)
    n=n//10
if num==sum:
    print("armstrong")
else:
    print("not armstrong")