# Understanding Input Handling
user_input = input("Enter a sentence or paragraph: ")

# String Manipulation
def count_words(input_text):
    """Count the number of words in the input text."""
    words = input_text.split()
    return len(words)

# Function Creation
word_count = count_words(user_input)

# Basic Control Flow
if word_count > 0:
    # Output Display
    print(f"Word count: {word_count}")
else:
    # Error Handling
    print("Error: Empty input. Please enter a valid sentence or paragraph.")
