"""Chapter 11: Graphs"""
from collections import defaultdict,deque
import heapq

class UnionFind:
    def __init__(self,n): self.p=list(range(n));self.r=[0]*n
    def find(self,x):
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py: return False
        if self.r[px]<self.r[py]: px,py=py,px
        self.p[py]=px
        if self.r[px]==self.r[py]: self.r[px]+=1
        return True

def num_islands(grid):
    if not grid: return 0
    rows,cols=len(grid),len(grid[0]);cnt=0
    def bfs(r,c):
        q=deque([(r,c)]);grid[r][c]='0'
        while q:
            y,x=q.popleft()
            for dy,dx in[(0,1),(0,-1),(1,0),(-1,0)]:
                ny,nx=y+dy,x+dx
                if 0<=ny<rows and 0<=nx<cols and grid[ny][nx]=='1':
                    grid[ny][nx]='0';q.append((ny,nx))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1': bfs(r,c);cnt+=1
    return cnt

def find_order(n,prereqs):
    g=defaultdict(list);ind=[0]*n
    for a,b in prereqs: g[b].append(a);ind[a]+=1
    q=deque([i for i in range(n) if ind[i]==0]);order=[]
    while q:
        v=q.popleft();order.append(v)
        for nb in g[v]: ind[nb]-=1;(q.append(nb) if ind[nb]==0 else None)
    return order if len(order)==n else []

def network_delay(times,n,k):
    g=defaultdict(list)
    for u,v,w in times: g[u].append((w,v))
    dist={k:0};h=[(0,k)]
    while h:
        d,nd=heapq.heappop(h)
        if d>dist.get(nd,float('inf')): continue
        for w,nb in g[nd]:
            nd2=d+w
            if nd2<dist.get(nb,float('inf')): dist[nb]=nd2;heapq.heappush(h,(nd2,nb))
    return max(dist.values()) if len(dist)==n else -1

if __name__=="__main__":
    grid=[['1','1','0'],['0','1','0'],['0','0','1']]
    print("Islands:", num_islands(grid))
    print("Course Order:", find_order(4,[[1,0],[2,0],[3,1],[3,2]]))
    print("Network Delay:", network_delay([[2,1,1],[2,3,1],[3,4,1]],4,2))
