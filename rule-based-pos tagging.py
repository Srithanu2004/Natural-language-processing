import re

# Define simple POS tagging rules using regex
rules = [
    (r'\d+', 'NUM'),  # Numbers
    (r'.*ing$', 'VERB'),  # Verbs ending in "ing"
    (r'.*ed$', 'VERB'),  # Past tense verbs
    (r'.*s$', 'NOUN'),  # Plural nouns
    (r'^(is|am|are|was|were)$', 'VERB'),  # Be verbs
    (r'^(a|an|the)$', 'DET'),  # Determiners
    (r'^(on|in|at|by|with)$', 'PREP'),  # Prepositions
    (r'.*', 'NOUN')  # Default to noun
]

# Function to tag words
def pos_tagger(words):
    tagged_words = []
    for word in words:
        for pattern, tag in rules:
            if re.fullmatch(pattern, word):
                tagged_words.append((word, tag))
                break
    return tagged_words

# Sample sentence
sentence = "The cat is running in the garden"
words = sentence.split()  # Simple tokenization

# Tag words
tagged = pos_tagger(words)

# Output
print(tagged)
