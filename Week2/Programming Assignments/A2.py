a = int(input())
b = int(input())
c = int(input())

if(a*a == b*b + c*c):
    print("YES", end="")
elif(b*b == a*a + c*c):
    print("YES", end="")
elif(c*c == a*a + b*b):
    print("YES", end="")
else: print("NO", end="")