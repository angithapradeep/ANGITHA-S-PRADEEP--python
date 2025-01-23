#prime numbers within a range
lb=int(input("enter the lower bound :"))
ub=int(input("enter the upper bound :"))
count=0
print("the prime numbers are :")
for i in range(lb,ub+1):
    for j in range(2,i):
        if i%j==0:
            count+=1
            break   
    if count==0:
        print(i)
    count=0
    

