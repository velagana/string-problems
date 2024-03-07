# Taking input from the user
lower = int(input("Enter lower bound of the interval: "))
upper = int(input("Enter upper bound of the interval: "))

print("Prime numbers between", lower, "and", upper, "are:")

# Iterating through the interval to check for prime numbers
for num in range(lower, upper + 1):
    # Prime numbers are greater than 1
    if num > 1:
        is_prime = True
        # Checking if the number is divisible by any number from 2 to its square root
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        # If the number is prime, print it
        if is_prime:
            print(num)
