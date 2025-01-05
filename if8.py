#find the largest of 3 numbers
a=int(input("enter the number1 :"))
b=int(input("enter the number2 :"))
c=int(input("enter the number3 :"))
if a>b and a>c:
    print(f"the largest number is {a}")
elif b>a and b>c:
    print(f"the largest number is {b}")
else:
    print("largest number is ",c)