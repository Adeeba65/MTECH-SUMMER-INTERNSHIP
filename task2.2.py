# Task 2.2: Multiplication Table (1 to 10)
num = int(input("Enter a number for multiplication table: "))

print(f"\n Multiplication Table of {num}")
print("-" * 20)

for i in range(1, 11):
    print(f"{num} × {i:2} = {num * i:3}")