#e^x = 1+x+x^2 /2! + x^3/3!................
sum=1
fact=1
n=int(input("enter the number of terms :"))
x=int(input("enter the value of x :"))
for i in range(1,n+1):
    fact*=i
    sum+=(x**i)/fact
print(f"{sum:.4f}")