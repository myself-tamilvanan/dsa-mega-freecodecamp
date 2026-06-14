"""LC 322 - Coin Change"""
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for amt in range(1, amount+1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], dp[amt-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_ways(coins, amount):
    """LC 518 - Count ways (combinations)"""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:        # outer = coin to avoid duplicates
        for amt in range(coin, amount+1):
            dp[amt] += dp[amt - coin]
    return dp[amount]

if __name__ == "__main__":
    cases = [([1,5,11],15), ([2],3), ([1,2,5],11), ([186,419,83,408],6249)]
    for coins, amount in cases:
        mc = coin_change(coins, amount)
        cw = coin_change_ways(coins, amount)
        print(f"coins={coins}, amount={amount} -> min={mc}, ways={cw}")
