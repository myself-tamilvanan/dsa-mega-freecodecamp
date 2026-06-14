"""LC 242 - Valid Anagram"""
from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t): return False
    return Counter(s) == Counter(t)

def is_anagram_v2(s, t):
    """Without Counter — manual counting"""
    if len(s)!=len(t): return False
    freq = {}
    for c in s: freq[c] = freq.get(c,0)+1
    for c in t:
        if c not in freq or freq[c]==0: return False
        freq[c]-=1
    return True

if __name__=="__main__":
    cases = [("anagram","nagaram"),("rat","car"),("listen","silent")]
    for s,t in cases:
        print(f"'{s}' & '{t}': {is_anagram(s,t)}")
