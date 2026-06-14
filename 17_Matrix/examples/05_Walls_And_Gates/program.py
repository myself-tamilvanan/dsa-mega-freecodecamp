"""LC 286 - Walls & Gates"""
from collections import deque
INF=2**31-1
def walls_and_gates(rooms):
    rows,cols=len(rooms),len(rooms[0])
    q=deque([(r,c) for r in range(rows) for c in range(cols) if rooms[r][c]==0])
    while q:
        r,c=q.popleft()
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc]==INF:
                rooms[nr][nc]=rooms[r][c]+1;q.append((nr,nc))
    return rooms
if __name__=="__main__":
    grid=[[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
    result=walls_and_gates([r[:] for r in grid])
    print("Walls & Gates result:")
    for row in result: print([x if x!=INF else 'INF' for x in row])
