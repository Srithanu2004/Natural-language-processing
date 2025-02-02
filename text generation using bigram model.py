import random
from collections import defaultdict

class BigramModel:
    def __init__(self):
        # Dictionary to store bigrams and their frequencies
        self.bigrams = defaultdict(lambda: defaultdict(int))
        # List to store starting words for text generation
        self.start_words = []

    def train(self, text):
        # Split the text into words
        words = text.split()

        # Store the first word as a starting word
        self.start_words.append(words[0])

        # Build the bigram model
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.bigrams[current_word][next_word] += 1

    def generate_text(self, length=10):
        # Start with a random starting word
        current_word = random.choice(self.start_words)
        text = [current_word]

        for _ in range(length - 1):
            # If the current word has no next word in the bigram model, stop
            if current_word not in self.bigrams:
                break

            # Choose the next word based on the bigram probabilities
            next_word = self._choose_next_word(current_word)
            text.append(next_word)
            current_word = next_word

        return ' '.join(text)

    def _choose_next_word(self, current_word):
        # Get the possible next words and their counts
        next_words = self.bigrams[current_word]
        total_count = sum(next_words.values())

        # Choose a random word based on the probability distribution
        rand_val = random.uniform(0, total_count)
        cumulative = 0
        for word, count in next_words.items():
            cumulative += count
            if rand_val <= cumulative:
                return word

        return None

# Example usage
if __name__ == "__main__":
    # Sample text for training
    text = (
        "I love to eat pizza. I love to drink coffee. I love to play games. "
        "I love to read books. I love to watch movies. I love to travel. "
        "I love to learn new things. I love to write code."
    )

    # Create and train the bigram model
    bigram_model = BigramModel()
    bigram_model.train(text)

    # Generate text using the bigram model
    generated_text = bigram_model.generate_text(length=15)
    print("Generated Text:", generated_text)
