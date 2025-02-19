import re

class FOPCParser:
    def _init_(self):
        # Define a basic grammar for predicates, quantifiers, and variables
        self.predicate_pattern = r'[A-Za-z_][A-Za-z0-9_]\([A-Za-z_][A-Za-z0-9_]\)'
        self.quantifier_pattern = r'(∀|∃)[A-Za-z_][A-Za-z0-9_]*'
        self.variable_pattern = r'[A-Za-z_][A-Za-z0-9_]*'
        self.expression_pattern = r'(' + self.quantifier_pattern + r'\s*' + self.predicate_pattern + r')|(' + self.predicate_pattern + ')'

    def parse(self, expression):
        # Check if the expression matches the pattern
        match = re.match(self.expression_pattern, expression)
        if match:
            print(f"Valid FOPC expression: {expression}")
            self.evaluate(expression)
        else:
            print(f"Invalid FOPC expression: {expression}")

    def evaluate(self, expression):
        # Evaluate a basic logical expression
        if re.match(self.quantifier_pattern, expression):
            quantifier = re.match(self.quantifier_pattern, expression).group(0)
            print(f"Quantifier: {quantifier}")
            rest_of_expression = expression[len(quantifier):].strip()
            predicate_match = re.match(self.predicate_pattern, rest_of_expression)
            if predicate_match:
                print(f"Predicate: {predicate_match.group(0)}")
            else:
                print("No valid predicate found after quantifier.")
        elif re.match(self.predicate_pattern, expression):
            print(f"Predicate: {expression}")
        else:
            print("Invalid expression.")
        
# Example Usage:
parser = FOPCParser()

# Test valid expressions
parser.parse("∀x P(x)")  # Universal quantification
parser.parse("∃x Q(x)")  # Existential quantification
parser.parse("P(x)")  # Predicate with variable

# Test invalid expressions
parser.parse("∀xP(x")  # Missing closing parenthesis
parser.parse("P()")  # Predicate with empty argument
