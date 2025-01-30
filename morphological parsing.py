class FSMPluralizer:
    def __init__(self):
        self.transitions = {
            "y": lambda word: word[:-1] + "ies" if not word[-2] in "aeiou" else word + "s",
            "s": lambda word: word + "es" if word.endswith(("s", "x", "z", "ch", "sh")) else word + "s",
            "default": lambda word: word + "s"
        }
    
    def pluralize(self, word):
        if word.endswith("y"):
            return self.transitions["y"](word)
        elif word.endswith(("s", "x", "z", "ch", "sh")):
            return self.transitions["s"](word)
        else:
            return self.transitions["default"](word)

# Sample words
words = ["cat", "dog", "bus", "box", "baby", "church"]

# Create FSMPluralizer instance
fsm = FSMPluralizer()
pluralized_words = {word: fsm.pluralize(word) for word in words}

# Print results
print("Pluralized Words:", pluralized_words)
