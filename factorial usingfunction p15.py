# print factorial number using function
# Enrollment number : 92400527179
# Name : Nency Ishani

def factorial(num):
    fact = 1
    

    for i in range(1,num+1):
        fact = fact * i
    print("fact is : ",fact)


num = int(input("Enter number: "))
factorial(num)
    
   
























def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))



