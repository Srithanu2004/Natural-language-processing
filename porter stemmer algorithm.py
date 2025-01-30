def simple_stem(word):
    suffixes = {"ing": "", "ies": "y", "s": ""}
    for suffix, replacement in suffixes.items():
        if word.endswith(suffix):
            return word[:-len(suffix)] + replacement
    return word

# Sample words
words = ["running", "flies", "cats", "wolves", "babies", "churches"]

# Perform stemming
stemmed_words = {word: simple_stem(word) for word in words}

# Print results
print("Stemmed Words:", stemmed_words)

