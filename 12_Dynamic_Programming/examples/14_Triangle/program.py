from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # 11
    print(sol.minimumTotal([[-10]]))  # -10
    print(sol.minimumTotal([[1],[2,3]]))  # 3
