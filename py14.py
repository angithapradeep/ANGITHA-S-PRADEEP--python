#armstrong or not
n=int(input("enter a 3-digit number :"))
sum=0
num=n
while(n>0):
    rem=n%10
    sum+=rem*rem*rem
    n=n//10
if sum==num:
    print("armstrong//")
else:
    print("not armstrong//")