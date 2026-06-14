"""LC 49 - Group Anagrams"""
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

def group_anagrams_v2(strs):
    """Using character frequency as key"""
    groups = defaultdict(list)
    for s in strs:
        key = [0]*26
        for c in s: key[ord(c)-ord('a')]+=1
        groups[tuple(key)].append(s)
    return list(groups.values())

if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print("Group Anagrams:", group_anagrams(strs))
    strs2 = ["","b",""]
    print("Edge case:", group_anagrams(strs2))
