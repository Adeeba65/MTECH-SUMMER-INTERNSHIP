# Task 4.1: Function to calculate factorial
def factorial(n):
    """Calculate factorial of a number using recursion"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
num = int(input("Enter a number for factorial: "))
result = factorial(num)
print(f"Factorial of {num} = {result}")