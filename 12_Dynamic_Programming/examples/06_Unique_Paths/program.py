"""LC 62 & 63 - Unique Paths I and II"""
def unique_paths(m, n):
    """LC 62 - No obstacles"""
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    return dp[-1]

def unique_paths_with_obstacles(grid):
    """LC 63 - With obstacles"""
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1 if grid[0][0] == 0 else 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1: dp[j] = 0
            elif j > 0: dp[j] += dp[j-1]
    return dp[-1]

if __name__ == "__main__":
    print("Unique Paths:")
    for m,n in [(3,7),(3,2),(1,1),(10,10)]:
        print(f"  {m}x{n} = {unique_paths(m,n)}")
    print("\nWith Obstacles:")
    grids=[ [[0,0,0],[0,1,0],[0,0,0]], [[0,1],[0,0]], [[1,0]] ]
    for g in grids:
        print(f"  {g} -> {unique_paths_with_obstacles(g)}")
