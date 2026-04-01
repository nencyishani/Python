#function to create function which accepts 3 argument
#Name:Nency Ishani ;  Enrolment no: 92400527179

def arithmetic(a,b,op):
    if op == '+' :
        print("addition:  ",a+b)

    elif op == '-':
        print("subtration:  ",a-b)

    elif op == '*':
        print("multiplication: ",a*b)

    elif op == '/':
+        print("division:  ",a/b)

    elif op == '%' :
        print("moduls:  ",a%b)

    else :
        print("Invaild Oprator")


a = int(input("enter first number:  "))
b = int(input("enter second number:  "))
op = input("+,-,*,/,%:  ")

arithmetic(a,b,op)
