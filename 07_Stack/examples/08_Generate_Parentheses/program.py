"""LC 22 - Generate Parentheses"""
def generate_parenthesis(n):
    result = []
    def backtrack(s, open_c, close_c):
        if len(s) == 2*n:
            result.append(s); return
        if open_c < n:
            backtrack(s+'(', open_c+1, close_c)
        if close_c < open_c:
            backtrack(s+')', open_c, close_c+1)
    backtrack("", 0, 0)
    return result

if __name__ == "__main__":
    for n in [1, 2, 3]:
        combos = generate_parenthesis(n)
        print(f"n={n}: {len(combos)} combinations: {combos}")
