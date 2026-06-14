"""LC 5 - Longest Palindromic Substring"""
def longest_palindrome(s):
    start = max_len = 0
    n = len(s)
    def expand(l, r):
        nonlocal start, max_len
        while l>=0 and r<n and s[l]==s[r]:
            if r-l+1 > max_len:
                max_len = r-l+1; start = l
            l-=1; r+=1
    for i in range(n):
        expand(i, i)
        expand(i, i+1)
    return s[start:start+max_len]

if __name__=="__main__":
    cases = ["babad","cbbd","a","ac","racecar","noon"]
    for s in cases:
        print(f"'{s}' -> '{longest_palindrome(s)}'")
