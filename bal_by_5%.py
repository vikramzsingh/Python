#Check balance if balance is Greater than 10000,if balance>10000 give bonus by5% else by2%.

bal=int(input("Enter the balance: "))

if(bal>10000):
    bonus=bal*0.05
else:
    bonus=bal*0.02

print("your Balance:",bal)
print("The Bonus:",bonus)
t=bal+bonus
print("Total Balance:",t)
