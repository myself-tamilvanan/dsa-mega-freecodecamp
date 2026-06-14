"""LC 338 - Counting Bits"""
def count_bits(n):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

if __name__ == "__main__":
    for n in [5, 10, 16]:
        result = count_bits(n)
        print(f"n={n}: {result}")
        print(f"  Verification: {[bin(i).count('1') for i in range(n+1)]}")
        print(f"  Match: {result == [bin(i).count('1') for i in range(n+1)]}")
