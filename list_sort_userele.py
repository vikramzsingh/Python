#insert elements in the list by user and sort it and print

lst=[]
n=int(input("Enter the size of list: "))

for i in range(0,n,1):
    ele=int(input("Enter the element: "))
    lst.append(ele)

print("The list is: ",lst)

for i in range(0,n,1):
    for j in range(0,n-1,1):
        if(lst[j]>lst[j+1]):
            m=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=m

print("The Sorted list: ")
for i in range(0,n,1):
    print(lst[i],end=",")
    
