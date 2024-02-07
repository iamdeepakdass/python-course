num = int(input("Enter a number: "))

result = 1
counter = 1
while(counter <= num):
    result *= counter
    counter += 1

print("Factorial of",num, "is", result)