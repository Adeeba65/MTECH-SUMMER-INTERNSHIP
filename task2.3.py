# Task 2.3: Keep adding numbers until user enters 0
total = 0
count = 0

print(" Enter numbers to add (enter 0 to stop):")

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total += num
    count += 1

print(f"\n Total numbers entered: {count}")
print(f" Sum of all numbers: {total}")