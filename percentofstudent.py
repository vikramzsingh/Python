# WAP to calculate percentage of student.
e=int(input("Enter marks in english:"))
p=int(input("Enter marks in physics:"))
c=int(input("Enter marks in Chemistry:"))
m=int(input("Enter marks in math"))
gk=int(input("Enter marks in gk"))

t=int(500)

percent=(e+p+c+m+gk)/t*100

print("The percent is :",percent)