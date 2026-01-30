#Write a program to print total marks
#Roll no:92400527179,Name:Nency Ishani
m1=int(input("Enter marks of sub1:"))
m2=int(input("Enter marks of sub2:"))
m3=int(input("Enter marks of sub3:"))
m4=int(input("Enter marks of sub4:"))

total= m1+m2+m3+m4
per=total/4

if m1<40 or m2<40 or m3<40 or m4<40:
    result="FAIL"
    grade="NO GRADE"
else:
    result="PASS"
if per >= 95:
        print("grade = A+ ")

elif per >= 70:
        print("grade = B+ ")

elif per >= 50:
        print("grade = B ")

elif per >= 40:
        print("grade = C ")

