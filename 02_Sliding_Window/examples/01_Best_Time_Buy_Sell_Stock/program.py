"""LC 121 - Best Time to Buy and Sell Stock"""
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

if __name__=="__main__":
    cases = [[7,1,5,3,6,4],[7,6,4,3,1],[1],[2,4,1]]
    for p in cases:
        print(f"{p} -> max profit: {max_profit(p)}")
