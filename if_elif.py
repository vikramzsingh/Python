#Scholarship
#class 12th per%>=60 then 4000 otherwise 3000
#class 10th per%>=60 then 2500 otherwise 1500
cl=int(input("Enter the class: "))
per=int(input("Enter the percentage: "))
if(cl==12):
    if(per>=60):
        amt=4000
    else:
        amt=3000
elif(cl==10):
    if(per>=60):
        amt=2500
    else:
        amt=1500

print("The Scholarship is:",amt)

