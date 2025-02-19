# Define a Probabilistic Context-Free Grammar (PCFG)
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [0.95] | VP [0.05]
    NP -> Det N [0.6] | N [0.4]
    VP -> V NP [0.7] | V [0.3]
    Det -> 'the' [1.0]
    N -> 'dog' [0.7] | 'cat' [0.3]
    V -> 'barked' [0.8] | 'chased' [0.2]
""")

# Create a Viterbi parser
parser = nltk.ViterbiParser(pcfg_grammar)

# Define the sentence to parse
sentence = "the dog barked".split()

# Parse the sentence and display the most probable parse tree
for tree in parser.parse(sentence):
    tree.pretty_print()
