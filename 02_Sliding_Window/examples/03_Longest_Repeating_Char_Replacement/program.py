"""LC 424 - Longest Repeating Character Replacement"""
from collections import defaultdict

def character_replacement(s, k):
    count = defaultdict(int)
    l = max_freq = result = 0
    for r, c in enumerate(s):
        count[c] += 1
        max_freq = max(max_freq, count[c])
        while (r-l+1) - max_freq > k:
            count[s[l]] -= 1
            l += 1
        result = max(result, r-l+1)
    return result

if __name__=="__main__":
    cases = [("ABAB",2),("AABABBA",1),("AAAA",2)]
    for s,k in cases:
        print(f"s='{s}', k={k} -> {character_replacement(s,k)}")
