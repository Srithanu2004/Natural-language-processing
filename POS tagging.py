import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download NLTK data (only needed the first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform POS tagging
    pos_tags = pos_tag(words)

    return pos_tags

# Example usage
if __name__ == "__main__":
    # Input text
    text = "Natural Language Processing is a fascinating field of study."

    # Perform POS tagging
    tagged_text = pos_tagging(text)

    # Print the result
    print("POS Tagging Result:")
    for word, tag in tagged_text:
        print(f"{word}: {tag}")
