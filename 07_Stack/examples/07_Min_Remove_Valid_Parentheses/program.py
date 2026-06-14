"""LC 1249 - Minimum Remove to Make Valid Parentheses"""
def min_remove_to_make_valid(s):
    stack = []  # indices of unmatched '('
    to_remove = set()
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)  # unmatched ')'
    to_remove |= set(stack)  # unmatched '('
    return ''.join(c for i, c in enumerate(s) if i not in to_remove)

if __name__ == "__main__":
    cases = ["lee(t(c)o)de)", "a)b(c)d", "))(("]
    for s in cases:
        result = min_remove_to_make_valid(s)
        print(f"'{s}' -> '{result}'")
