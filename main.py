print("Calculate Factorial")

n = int(input("Enter a number (1-10)\n"))

result = 1
for i in range(1,n+1):
    if(n == 0):
        result=1
        break
    result *= i

print("Result is: ",result)