# creates a class with function overloading
# Enrollment Number : 92400527179
# Name : Nency  ishani

class calculator:
    def addition(self,*args):
        return sum(args)

c =  calculator()
print(c.addition(5))
print(c.addition(5,10))
print(c.addition(5,10,15))
print(c.addition(5,10,15,20))
