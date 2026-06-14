"""LC 678 - Valid Parenthesis String"""
def check_valid_string(s):
    min_open = max_open = 0
    for c in s:
        if c == '(':   min_open += 1; max_open += 1
        elif c == ')': min_open -= 1; max_open -= 1
        else:          min_open -= 1; max_open += 1  # '*'
        if max_open < 0: return False
        min_open = max(0, min_open)
    return min_open == 0

if __name__ == "__main__":
    cases = ["(*)","(*))","(()","()","(*","(*(","*","***"]
    for s in cases:
        print(f"'{s}' -> {check_valid_string(s)}")
