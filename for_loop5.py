#Print even number with for loop

n=int(input("Enter the number: "))

for i in range(1,n,1):
    if(i%2!=0):
        print(i,end=" ")
