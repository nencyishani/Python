# Write a program to read names from keyboard and store into text file
# Enrollment number : 92400527179
# Name : Nency ishani

file = open("names.txt","w")

n = int(input("how many names do you want to enter: "))

for i in range(n):
    name = input("Enter name: ")
    file.write(name + "\n")

file.close()

print("Names saved successfully")
