def fsa_match_ab(string):
    state = 'q0'  # Initial state
    
    for char in string:
        if state == 'q0':
            if char == 'a':
                state = 'q1'
        elif state == 'q1':
            if char == 'b':
                state = 'q2'
            elif char != 'a':  # Any other character resets to q0
                state = 'q0'
        elif state == 'q2':
            if char == 'a':  # Handle cases like "aba"
                state = 'q1'
            else:
                state = 'q0'
    
    # Final state check
    return "Accepted" if state == 'q2' else "Rejected"

# Test cases
test_strings = ["ab", "aab", "baba", "abc", "abab", "ba", "b"]
for s in test_strings:
    print(f"String '{s}' → {fsa_match_ab(s)}")
