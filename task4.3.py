# Task 4.3: Function to reverse a string without using [::-1]
def reverse_string(text):
    """Reverse a string manually using a loop"""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# Test the function
text = input("Enter a string to reverse: ")
result = reverse_string(text)
print(f"Original: {text}")
print(f"Reversed: {result}")