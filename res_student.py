#To check is student pass or not.Passing marks is 40%

e=int(input("Enter the marks in English: "))
p=int(input("Enter the marks in Physics: "))
c=int(input("Enter the marks in Chemistry: "))
m=int(input("Enter the marks in Math: "))
gk=int(input("Enter the marks in GK: "))
t=500

percent=(e+p+c+m+gk)*100/t

if(percent>=40):
    print("Pass with percentage:",percent,"percentage")
else:
    print("fail try again")
