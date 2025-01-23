#youngest and eldest of 3 individuals
ind1=int(input("enter the age of 1st person :"))
ind2=int(input("enter the age of 2nd person :"))
ind3=int(input("enter the age of 3rd person :"))
if ind1>ind2 and ind1>ind3:
    print("person1 is the oldest!!!!")
elif ind2>ind1 and ind2>ind3:
    print("person2 is the oldest!!!! ")
else:
    print("person3 is the oldest!!!!")
if ind1 <= ind2 and ind1 <= ind3:
    youngest = ind1
elif ind2 <= ind1 and ind2 <= ind3:
    youngest = ind2
else:
    youngest = ind3
print("The youngest is:", youngest)
