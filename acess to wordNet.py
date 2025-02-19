import nltk
from nltk.corpus import wordnet as wn

# Download WordNet data (if not already installed)
nltk.download('wordnet')

# Input word
word = "bank"

# Retrieve synsets for the word
synsets = wn.synsets(word)

# Display synsets and their meanings
print(f"Synsets for the word '{word}':")
for synset in synsets:
    print(f"\nSynset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")
