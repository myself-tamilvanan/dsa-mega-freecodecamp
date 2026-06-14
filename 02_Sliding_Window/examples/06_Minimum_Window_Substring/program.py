"""LC 76 - Minimum Window Substring"""
from collections import Counter, defaultdict

def min_window(s, t):
    if not t or not s: return ""
    need = Counter(t)
    window = defaultdict(int)
    have, total = 0, len(need)
    l = 0
    best = ""
    for r, c in enumerate(s):
        window[c] += 1
        if c in need and window[c] == need[c]:
            have += 1
        while have == total:
            if not best or (r - l + 1) < len(best):
                best = s[l:r+1]
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1
    return best

if __name__ == "__main__":
    cases = [("ADOBECODEBANC","ABC","BANC"),("a","a","a"),("a","aa",""),("aa","aa","aa")]
    for s,t,expected in cases:
        result = min_window(s,t)
        print(f"s='{s}', t='{t}' -> '{result}' {'✓' if result==expected else f'✗ expected {expected}'}")
