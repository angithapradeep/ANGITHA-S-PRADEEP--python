#all prime numbers till 1000
count=0
print(2)
for i in range(2,1001):
    count=0
    for j in range(2,i):
        if i%j==0:
            break
        else:
            count+=1
    if count!=0:
        print(i)
        
    