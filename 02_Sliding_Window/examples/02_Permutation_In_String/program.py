"""LC 567 - Permutation in String"""
from collections import Counter

def check_inclusion(s1, s2):
    if len(s1) > len(s2): return False
    need = Counter(s1)
    window = Counter(s2[:len(s1)])
    if window == need: return True
    for i in range(len(s1), len(s2)):
        window[s2[i]] += 1
        c = s2[i-len(s1)]
        window[c] -= 1
        if window[c] == 0: del window[c]
        if window == need: return True
    return False

if __name__=="__main__":
    cases=[("ab","eidbaooo"),("ab","eidboaoo"),("adc","dcda")]
    for s1,s2 in cases:
        print(f"s1='{s1}', s2='{s2}' -> {check_inclusion(s1,s2)}")
