#print consonants in a given string
str=input("enter the string :")
for i in str:
    if i not in 'AEIOUaeiou':
       print(i,end=' ')