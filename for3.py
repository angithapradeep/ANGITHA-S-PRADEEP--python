#python prgm to print the multipilication table of a given number
abc=int(input("enter the number :"))
print(f"the multiplication table of {abc} is :")
for i in range(1,11):
    print(abc," * ",i," = ",abc*i)
print("------------------------")
