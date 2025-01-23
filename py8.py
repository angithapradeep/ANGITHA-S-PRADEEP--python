#all numbers from 100 to 1000 whose sum of digits is divisble by 9
rem=0
for num in range(100,1001):
    sum=0
    i=num
    while(i>0):
        rem=i%10
        sum+=rem
        i=i//10
    if sum%9==0:
        print(num)
    
    
    