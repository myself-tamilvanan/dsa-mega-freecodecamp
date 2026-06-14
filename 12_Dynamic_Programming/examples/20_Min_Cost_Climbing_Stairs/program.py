from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2 = cost[0]
        prev1 = cost[1]
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr
        return min(prev1, prev2)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([10,15,20]))                          # 15
    print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))        # 6
    print(sol.minCostClimbingStairs([0,0,0,0]))                           # 0
