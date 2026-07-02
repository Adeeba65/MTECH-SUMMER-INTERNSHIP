# Task 2.1: Check if a number is prime
num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a PRIME number ")
    else:
        print(f"{num} is NOT a prime number ")
else:
    print(f"{num} is NOT a prime number ")