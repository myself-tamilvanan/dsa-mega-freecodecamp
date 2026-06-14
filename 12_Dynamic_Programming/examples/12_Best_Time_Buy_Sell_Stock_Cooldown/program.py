from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # States: holding, sold (just sold, cooldown next), idle (can buy)
        holding = float('-inf')
        sold = 0
        idle = 0
        for price in prices:
            prev_sold = sold
            sold = holding + price       # sell today
            holding = max(holding, idle - price)  # buy today (from idle state)
            idle = max(idle, prev_sold)  # cooldown over
        return max(sold, idle)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1,2,3,0,2]))  # 3
    print(sol.maxProfit([1]))           # 0
    print(sol.maxProfit([2,1,4]))       # 3
