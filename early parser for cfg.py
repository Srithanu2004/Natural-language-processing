from collections import defaultdict

class EarleyParser:
    def __init__(self, grammar):
        self.grammar = self.process_grammar(grammar)
        self.start_symbol = list(self.grammar.keys())[0]

    def process_grammar(self, grammar):
        processed_grammar = defaultdict(list)
        for rule in grammar:
            lhs, rhs = rule.split(" -> ")
            for production in rhs.split(" | "):
                processed_grammar[lhs].append(production.split())
        return processed_grammar

    def predict(self, state_set, rule, index):
        if rule in self.grammar:
            for production in self.grammar[rule]:
                state = (rule, production, 0, index)
                if state not in state_set:
                    state_set.append(state)

    def scan(self, state_set, state, word):
        lhs, rhs, dot, origin = state
        if dot < len(rhs) and rhs[dot] == word:
            new_state = (lhs, rhs, dot + 1, origin)
            if new_state not in state_set:
                state_set.append(new_state)

    def complete(self, state_sets, state_set, state):
        lhs, rhs, dot, origin = state
        if dot == len(rhs):
            for s in state_sets[origin]:
                s_lhs, s_rhs, s_dot, s_origin = s
                if s_dot < len(s_rhs) and s_rhs[s_dot] == lhs:
                    new_state = (s_lhs, s_rhs, s_dot + 1, s_origin)
                    if new_state not in state_set:
                        state_set.append(new_state)

    def parse(self, tokens):
        n = len(tokens)
        state_sets = [[] for _ in range(n + 1)]
        state_sets[0].append((self.start_symbol, ["E"], 0, 0))  

        for i in range(n + 1):
            j = 0
            while j < len(state_sets[i]):
                state = state_sets[i][j]
                lhs, rhs, dot, origin = state
                if dot < len(rhs) and rhs[dot] in self.grammar:
                    self.predict(state_sets[i], rhs[dot], i)
                elif dot < len(rhs) and i < n:
                    self.scan(state_sets[i + 1], state, tokens[i])
                else:
                    self.complete(state_sets, state_sets[i], state)
                j += 1  

        for state in state_sets[-1]:
            if state == (self.start_symbol, ["E"], 1, 0):
                return True  
        return False

grammar = [
    "E -> E + T | T",
    "T -> T * F | F",
    "F -> ( E ) | id"
]

parser = EarleyParser(grammar)
sentence = "id + id * id".split()
print("Accepted" if parser.parse(sentence) else "Rejected")

   
