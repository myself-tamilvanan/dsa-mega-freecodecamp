from typing import List
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        
        @lru_cache(maxsize=None)
        def dfs(r, c):
            best = 1
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best
        
        return max(dfs(r, c) for r in range(m) for c in range(n))

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # 4
    print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # 4
    print(sol.longestIncreasingPath([[1]]))  # 1
