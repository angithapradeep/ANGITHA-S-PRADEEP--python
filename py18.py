#number of odd numbers and even numbers in a set of numbers
l=[]
c1=0
c2=0
n=int(input("enter the count of numbers :"))
for i in range(0,n):
    num=int(input("enter the number:"))
    l.append(num)
print("the list is :",l)
for i in l:
    if i%2==0:
        c1+=1
    else:
        c2+=1
print("the number of odd numbers is",c2)
print("the number of even numbers is",c1)