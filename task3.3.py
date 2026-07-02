# Task 3.3: Word frequency counter
sentence = "I love Python because Python is easy"

# Split sentence into words
words = sentence.split()

# Create empty dictionary for frequency
word_count = {}

# Count frequency of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Print results
print(" Word Frequency Analysis")
print("-" * 30)
print(f"Original sentence: {sentence}")
print("\nWord frequencies:")
for word, count in word_count.items():
    print(f"  • '{word}': {count} time(s)")