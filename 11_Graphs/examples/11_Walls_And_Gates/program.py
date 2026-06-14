"""LC 286 - Walls & Gates"""
from collections import deque
INF=2**31-1

def walls_and_gates(rooms):
    rows,cols=len(rooms),len(rooms[0])
    q=deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c]==0: q.append((r,c))
    while q:
        r,c=q.popleft()
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc]==INF:
                rooms[nr][nc]=rooms[r][c]+1
                q.append((nr,nc))
    return rooms

if __name__=="__main__":
    grid=[[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
    result=walls_and_gates([row[:] for row in grid])
    for row in result: print(row)
