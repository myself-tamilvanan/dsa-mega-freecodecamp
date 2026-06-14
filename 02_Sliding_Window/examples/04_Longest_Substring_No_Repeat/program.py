"""LC 3 - Longest Substring Without Repeating Characters"""
def length_of_longest_substring(s):
    char_idx = {}
    l = result = 0
    for r, c in enumerate(s):
        if c in char_idx and char_idx[c] >= l:
            l = char_idx[c] + 1
        char_idx[c] = r
        result = max(result, r-l+1)
    return result

if __name__=="__main__":
    cases = ["abcabcbb","bbbbb","pwwkew","","au"]
    for s in cases:
        print(f"'{s}' -> {length_of_longest_substring(s)}")
