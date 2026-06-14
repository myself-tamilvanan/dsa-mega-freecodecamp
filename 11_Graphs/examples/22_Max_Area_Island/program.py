from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area

if __name__ == "__main__":
    sol = Solution()
    grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid1))  # 6
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))  # 0
    print(sol.maxAreaOfIsland([[1,1],[1,0]]))  # 3
