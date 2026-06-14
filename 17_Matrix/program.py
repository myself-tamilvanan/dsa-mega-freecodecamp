"""Chapter 17: Matrix"""
from collections import deque

def set_zeroes(matrix):
    rows,cols=len(matrix),len(matrix[0])
    fr=any(matrix[0][j]==0 for j in range(cols))
    fc=any(matrix[i][0]==0 for i in range(rows))
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][j]==0: matrix[i][0]=matrix[0][j]=0
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][0]==0 or matrix[0][j]==0: matrix[i][j]=0
    if fr:
        for j in range(cols): matrix[0][j]=0
    if fc:
        for i in range(rows): matrix[i][0]=0
    return matrix

def oranges_rotting(grid):
    rows,cols=len(grid),len(grid[0]);q=deque();fresh=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==2: q.append((r,c,0))
            elif grid[r][c]==1: fresh+=1
    mins=0
    while q:
        r,c,t=q.popleft()
        for dr,dc in[(0,1),(0,-1),(1,0),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                grid[nr][nc]=2;fresh-=1;mins=t+1;q.append((nr,nc,t+1))
    return mins if fresh==0 else -1

def unique_paths(m,n):
    dp=[1]*n
    for _ in range(1,m):
        for j in range(1,n): dp[j]+=dp[j-1]
    return dp[-1]

if __name__=="__main__":
    print("Set Zeroes:", set_zeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print("Rotting Oranges:", oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]))
    print("Unique Paths 3x7:", unique_paths(3,7))
