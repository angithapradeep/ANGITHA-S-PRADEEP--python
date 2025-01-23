#A
#A B
#A B C
#A B C D
n=int(input("enter the number of rows :"))
s=65
for i in range(0,n):
    for j in range(i+1):
        print(chr(s),end=" ")
        s+=1
    s=65
    print()
