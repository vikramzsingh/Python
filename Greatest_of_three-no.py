#find max from three number
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
m=a

if(b>m):
    m=b
if(c>m):
    m=c

print("The greatest is: ",m)
    
