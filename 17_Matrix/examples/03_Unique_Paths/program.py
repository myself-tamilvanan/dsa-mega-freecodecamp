"""LC 62 - Unique Paths"""
def unique_paths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n): dp[j] += dp[j-1]
    return dp[-1]

def unique_paths_math(m, n):
    """Combinatorics: C(m+n-2, m-1)"""
    from math import comb
    return comb(m+n-2, m-1)

if __name__ == "__main__":
    print("Unique Paths:")
    for m,n in [(3,7),(3,2),(1,1),(10,10),(23,12)]:
        dp_result = unique_paths(m,n)
        math_result = unique_paths_math(m,n)
        print(f"  {m}x{n} -> dp={dp_result}, math={math_result}, equal={dp_result==math_result}")
