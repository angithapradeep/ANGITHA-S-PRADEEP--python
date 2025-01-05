#python program to calculate the sum of all numbers from 1 to a given range
lim=int(input("enter the limit :"))
sum=0
for i in range (1,lim+1):
    sum=sum+i
print(sum)