"""LC 198 & 213 - House Robber I and II"""
def rob_linear(nums):
    """LC 198 - Linear street"""
    prev2 = prev1 = 0
    for n in nums: prev2, prev1 = prev1, max(prev1, prev2+n)
    return prev1

def rob_circular(nums):
    """LC 213 - Circular street (first and last are adjacent)"""
    if len(nums) == 1: return nums[0]
    # Rob houses 0..n-2 OR 1..n-1
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

def rob_with_path(nums):
    """Return max amount AND which houses to rob"""
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    if n > 1: dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    # Backtrack to find chosen houses
    chosen = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            chosen.append(i); i -= 2
        else: i -= 1
    return dp[n-1], chosen[::-1]

if __name__ == "__main__":
    cases = [[1,2,3,1],[2,7,9,3,1],[2,1,1,2]]
    for nums in cases:
        linear = rob_linear(nums)
        circular = rob_circular(nums)
        amount, houses = rob_with_path(nums)
        print(f"{nums} -> linear={linear}, circular={circular}, houses={houses}")
