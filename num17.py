#program to check if a number is palindrome or not
n=int(input("enter the num to be checked :"))
num=n
rem=0
sum=0
while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
if num==sum:
    print("palindrome")
else:
    print("not palindrome")