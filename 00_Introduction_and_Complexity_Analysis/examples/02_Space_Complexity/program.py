"""Space Complexity Comparison"""
import sys

def sort_inplace(arr):
    """O(1) extra space - modifies in place"""
    arr.sort()
    return arr

def sort_merge(arr):
    """O(n) extra space - creates new arrays"""
    if len(arr) <= 1: return arr
    m = len(arr)//2
    return merge(sort_merge(arr[:m]), sort_merge(arr[m:]))

def merge(l, r):
    res, i, j = [], 0, 0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]: res.append(l[i]); i+=1
        else: res.append(r[j]); j+=1
    return res + l[i:] + r[j:]

def lcs_2d(s1, s2):
    """O(m*n) space - 2D DP table"""
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i-1][j-1]+1 if s1[i-1]==s2[j-1] else max(dp[i-1][j],dp[i][j-1])
    return dp[m][n], sys.getsizeof(dp)

if __name__ == "__main__":
    arr = [5,3,8,1,9,2,7,4,6]
    print("In-place sort (O(1) space):", sort_inplace(arr[:]))
    print("Merge sort (O(n) space):", sort_merge([5,3,8,1,9]))
    result, mem = lcs_2d("abcde", "ace")
    print(f"LCS (O(n²) space): result={result}, dp table size={mem} bytes")
