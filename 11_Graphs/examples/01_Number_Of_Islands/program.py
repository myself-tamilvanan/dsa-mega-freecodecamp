"""LC 200 - Number of Islands"""
from collections import deque

def num_islands_bfs(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    def bfs(r, c):
        q = deque([(r,c)]); grid[r][c]='0'
        while q:
            y,x = q.popleft()
            for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny,nx = y+dy, x+dx
                if 0<=ny<rows and 0<=nx<cols and grid[ny][nx]=='1':
                    grid[ny][nx]='0'; q.append((ny,nx))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1': bfs(r,c); count+=1
    return count

def num_islands_dfs(grid):
    if not grid: return 0
    rows,cols=len(grid),len(grid[0]); count=0
    def dfs(r,c):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!='1': return
        grid[r][c]='0'
        for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]: dfs(r+dy,c+dx)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1': dfs(r,c); count+=1
    return count

if __name__ == "__main__":
    import copy
    g1 = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
    g2 = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
    for g in [g1,g2]:
        print(f"Islands (BFS)={num_islands_bfs(copy.deepcopy(g))}, (DFS)={num_islands_dfs(copy.deepcopy(g))}")
