import nltk
from nltk import CFG

# Define a Context-Free Grammar with agreement rules
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N_sing | Det N_plur
    VP -> V_sing | V_plur
    Det -> 'the'
    N_sing -> 'cat' | 'dog'
    N_plur -> 'cats' | 'dogs'
    V_sing -> 'runs' | 'barks'
    V_plur -> 'run' | 'bark'
""")

# Function to check if a sentence follows subject-verb agreement
def check_agreement(sentence):
    words = sentence.split()  # Tokenize sentence
    parser = nltk.ChartParser(grammar)  # Create parser

    # Check if the sentence is valid in the given grammar
    try:
        parse_trees = list(parser.parse(words))
        if parse_trees:
            print(f"✅ The sentence '{sentence}' is grammatically correct!")
            for tree in parse_trees:
                tree.pretty_print()
        else:
            print(f"❌ The sentence '{sentence}' is incorrect.")
    except ValueError:
        print(f"❌ The sentence '{sentence}' is incorrect.")

# Test cases
check_agreement("the cat runs")   
check_agreement("the cats run")   
check_agreement("the cat run")    
check_agreement("the cats runs")  
