#write a program to print input age of person
#roll no:92400527179,Name:Nency Ishani

age= int(input("Enter your age:"))

if age<15:
    print("you are kid")
elif age>= 15 and age<= 18:
    print("you are tenage")
elif age>=18 and age<=60:
    print("you are adult")
else:
    print("you are senior citizen")
