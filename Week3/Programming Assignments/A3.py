from datetime import datetime

name1 = input()
dob1 = datetime.strptime(input(), "%d-%m-%Y")

name2 = input()
dob2 = datetime.strptime(input(), "%d-%m-%Y")

if(dob1 > dob2 or (dob1 == dob2 and name1 < name2)):
    print(name1,end="")
else:
    print(name2,end="")
