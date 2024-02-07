m = int(input())
n = int(input())

if(m < n):
    print(m, end="")
else:
    while(m >= n):
        m -= n
    print(m, end="")