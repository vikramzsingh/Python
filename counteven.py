#count even no. in the list given by user

lst=[]

n=int(input("Enter the number of elements: "))

for i in range(0,n,1):
    ele=int(input("Enter the element of the list: "))
    lst.append(ele)

print("Element inputted in the list",lst)

print("Manual list: ")

for i in range(0,n,1):
    if(i==n-1):
        print(lst[i],end=" ")
    else:
        print(lst[i],end=",")

print()

count=0
for i in range(0,n,1):
    if(lst[i]%2==0):
        count=count+1
print(count)
        
