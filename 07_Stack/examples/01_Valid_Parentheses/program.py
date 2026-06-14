"""LC 20 - Valid Parentheses"""
def is_valid(s):
    stack = []
    pairs = {')':'(','}':'{',']':'['}
    for c in s:
        if c in pairs:
            if not stack or stack[-1]!=pairs[c]: return False
            stack.pop()
        else: stack.append(c)
    return not stack
if __name__=="__main__":
    for s in ["()","()[]{}", "(]", "([)]", "{[]}", ""]:
        print(f"'{s}' -> {is_valid(s)}")
