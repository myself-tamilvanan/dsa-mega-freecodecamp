"""LC 300 - Longest Increasing Subsequence"""
import bisect

def lis_dp(nums):
    """O(n²) DP with path reconstruction"""
    n = len(nums)
    dp = [1]*n; parent = [-1]*n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1; parent[i] = j
    # Reconstruct
    idx = dp.index(max(dp))
    path = []
    while idx != -1: path.append(nums[idx]); idx = parent[idx]
    return max(dp), path[::-1]

def lis_binary_search(nums):
    """O(n log n) patience sorting"""
    tails = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails): tails.append(n)
        else: tails[i] = n
    return len(tails)

if __name__ == "__main__":
    cases = [[10,9,2,5,3,7,101,18],[0,1,0,3,2,3],[7,7,7,7,7]]
    for nums in cases:
        length, path = lis_dp(nums)
        fast = lis_binary_search(nums)
        print(f"{nums}")
        print(f"  DP length={length}, path={path}")
        print(f"  BinarySearch length={fast}")
