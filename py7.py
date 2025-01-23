#all the prime factors of a given number
n=int(input("enter a number :"))
print("the prime factors of",n,"are :")
count=0
for i in range(2,n):
    if n%i==0:
        if i==2:
            print(2)
        else:
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    count+=1
            if count!=0:
                print(i)
                count=0
        
    