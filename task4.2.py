# Task 4.2: Function to check if a number is prime
def is_prime(n):
    """Returns True if number is prime, False otherwise"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is PRIME ")
else:
    print(f"{num} is NOT prime ")