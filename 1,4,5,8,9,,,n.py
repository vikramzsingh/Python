#print 1,4,5,....n

n=int(input("Enter the number: "))

i=1
while(i<=n):
    print(i)
    if(i%2==0):
        print(i)
    else:
        i=i+3
        print(i)
    i=i+1
