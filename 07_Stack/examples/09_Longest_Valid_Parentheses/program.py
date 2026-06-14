"""LC 32 - Longest Valid Parentheses"""
def longest_valid_parentheses(s):
    stack = [-1]  # base index
    max_len = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # new base
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

if __name__ == "__main__":
    cases = [("(()",2),(")()())",4),("",0),("()()",4),("(((((",0)]
    for s,expected in cases:
        result = longest_valid_parentheses(s)
        print(f"'{s}' -> {result} {'✓' if result==expected else f'✗ expected {expected}'}")
