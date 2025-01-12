#to print the fibonacci series
n=int(input("enter the number of terms :"))
a=0
b=1
sum=0
if n==1:
    print(a)
elif n==2:
    print(a,b,ends=" ")
elif n>2:
    print(a)
    print(b)
    for i in range(2,n):
        sum=a+b
        print(sum)
        a=b
        b=sum
else:
    print("no series to be printed!!!!!!")
        

