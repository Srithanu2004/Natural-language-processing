import re

# Sample text
text = "The quick brown fox jumps over the lazy dog. The fox is clever."

# Regular expression pattern to find the word "fox"
pattern = r"fox"

# Search for the pattern in the text
match = re.search(pattern, text)
if match:
    print(f"'fox' found at position: {match.start()}")

# Find all occurrences of the pattern
matches = re.findall(pattern, text)
print(f"Occurrences of 'fox': {matches}")

# Check if the text starts with "The"
if re.match(r"The", text):
    print("The text starts with 'The'.")

# Replace "fox" with "cat"
new_text = re.sub(pattern, "cat", text)
print(f"Modified text: {new_text}")
