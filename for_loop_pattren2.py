#Pattren with for loop

n=int(input("Enter the number: "))

for i in range(1,n+1,1):
    for j in range(1,n-i+2,1):
        print("*",end=" ")
    print()
