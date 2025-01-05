#simple operations on a calculator
num1=int(input("enter the first operand :"))
num2=int(input("enter the second operand"))
res=0
op=input("enter the operator :")
if op=="+":
    res=num1+num2
    print(res)
elif op=="-":
    if num1>num2:
        res=num1-num2
    elif num2>num1:
        res=num2-num1
    else:
        res=0
    print(res)
elif op=="*":
    res=num1*num2
    print(res)
elif op=="/":
    res=num1/num2
    print(res)
else:
    print("invalid operation!!!!!!!!!!!!!!")
