from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        def count_live(r, c):
            return sum(1 for dr,dc in dirs 
                      if 0<=r+dr<m and 0<=c+dc<n and abs(board[r+dr][c+dc])==1)
        
        for r in range(m):
            for c in range(n):
                live = count_live(r, c)
                if board[r][c] == 1 and live not in (2, 3):
                    board[r][c] = -1  # was live, now dead
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 2   # was dead, now live
        
        for r in range(m):
            for c in range(n):
                board[r][c] = 1 if board[r][c] > 0 else 0

if __name__ == "__main__":
    sol = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sol.gameOfLife(board)
    for row in board:
        print(row)
    # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
