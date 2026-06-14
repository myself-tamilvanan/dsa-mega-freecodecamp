"""LC 647 - Palindromic Substrings"""
def count_substrings(s):
    n = len(s)
    count = [0]
    def expand(l, r):
        while l>=0 and r<n and s[l]==s[r]:
            count[0] += 1; l-=1; r+=1
    for i in range(n):
        expand(i, i)    # odd length
        expand(i, i+1)  # even length
    return count[0]

if __name__=="__main__":
    cases = ["abc","aaa","abba","racecar"]
    for s in cases:
        print(f"'{s}' -> {count_substrings(s)} palindromic substrings")
