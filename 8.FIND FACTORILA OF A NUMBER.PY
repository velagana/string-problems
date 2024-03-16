n = int(input("Enter the number: "))
fact = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(2, n + 1):
        fact *= i
    print("The factorial of", n, "is", fact)
