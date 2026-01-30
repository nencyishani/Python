#Write a programto print compound intrest
#Roll no:92400527179,Name:Nency Ishani
p = float(input("Enter Amount: "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))


ci = p * (1 + r / 100) ** t - p


print("Compound Interest is:", ci)
