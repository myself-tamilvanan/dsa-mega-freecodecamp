"""LC 70 - Climbing Stairs & Variations"""
def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1): a, b = b, a+b
    return b

def climb_stairs_k_steps(n, k):
    """Can take 1..k steps at a time"""
    dp = [0]*(n+1); dp[0] = 1
    for i in range(1, n+1):
        for step in range(1, k+1):
            if i >= step: dp[i] += dp[i-step]
    return dp[n]

def min_cost_climbing_stairs(cost):
    """LC 746 - pay cost[i] to climb from step i"""
    n = len(cost)
    dp = cost[:]
    for i in range(2, n):
        dp[i] += min(dp[i-1], dp[i-2])
    return min(dp[-1], dp[-2])

if __name__ == "__main__":
    for n in [1,2,3,5,10]:
        print(f"climb_stairs({n}) = {climb_stairs(n)}")
    print()
    print("3-step variant:")
    for n in [3,5,10]:
        print(f"  k=3, n={n}: {climb_stairs_k_steps(n, 3)}")
    cost = [10,15,20]
    print(f"\nMin cost [10,15,20]: {min_cost_climbing_stairs(cost)}")
