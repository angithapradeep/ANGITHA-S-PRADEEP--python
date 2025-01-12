#to print the factorial of a given number
n=int(input("enter the number :"))
fact=1
for i in range (1,n+1):
    fact*=i
print("factorial of the number is",fact)
