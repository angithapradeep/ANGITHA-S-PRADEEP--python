#program to find the number of words in a string
str=input("enter the sentence :")
count=1
for i in str:
    if i==" ":
        count+=1
print("the number of words =",count)