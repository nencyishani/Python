#read any text file line by line
#Name:Nency Ishani,Erollment:92400527179

filename = input("enter file name: ")

with open(filename,"r") as file:
    for line in file:
        print(line,end="")
