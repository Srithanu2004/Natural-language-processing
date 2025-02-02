import re

# Step 1: Define simple initial POS tagging rules
def initial_pos_tagger(words):
    tags = []
    for word in words:
        if re.fullmatch(r'\d+', word):  # Numbers
            tags.append((word, 'NUM'))
        elif word.endswith('ing'):  # Verbs ending in "ing"
            tags.append((word, 'VERB'))
        elif word.endswith('ed'):  # Past tense verbs
            tags.append((word, 'VERB'))
        elif word.endswith('s') and word.lower() not in ["is", "was"]:  # Plural nouns (not verbs)
            tags.append((word, 'NOUN'))
        else:
            tags.append((word, 'NOUN'))  # Default tag
    return tags

# Step 2: Define transformation rules to correct initial tags
def apply_transformation_rules(tagged_words):
    transformed = []
    for i, (word, tag) in enumerate(tagged_words):
        # Rule: If a word is "is" or "was", change its tag to VERB
        if word in ["is", "was"]:
            tag = "VERB"
        # Rule: If a word is "the", change its tag to DET (determiner)
        elif word.lower() == "the":
            tag = "DET"
        transformed.append((word, tag))
    return transformed

# Sample sentence
sentence = "The cat is running in the garden"
words = sentence.split()  # Simple tokenization

# Step 1: Assign initial tags
initial_tags = initial_pos_tagger(words)

# Step 2: Apply transformation rules
final_tags = apply_transformation_rules(initial_tags)

# Output
print(final_tags)
