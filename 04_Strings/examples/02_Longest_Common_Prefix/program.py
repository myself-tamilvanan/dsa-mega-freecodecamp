"""LC 14 - Longest Common Prefix"""
def longest_common_prefix(strs):
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: return ""
    return prefix

if __name__=="__main__":
    cases=[["flower","flow","flight"],["dog","racecar","car"],[""],["ab","a"]]
    for strs in cases:
        print(f"{strs} -> '{longest_common_prefix(strs)}'")
