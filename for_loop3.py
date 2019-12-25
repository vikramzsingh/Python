#Display table of a given number by user

n=int(input("Enter the number: "))

for i in range(1,11,1):
     t=n*i
     print(n,"*",i,"=",t)
