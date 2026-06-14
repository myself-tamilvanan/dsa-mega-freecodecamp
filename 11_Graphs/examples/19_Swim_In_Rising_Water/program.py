"""LC 778 - Swim in Rising Water"""
import heapq

def swim_in_water(grid):
    n=len(grid)
    heap=[(grid[0][0],0,0)]
    visited={(0,0)}
    while heap:
        t,r,c=heapq.heappop(heap)
        if r==n-1 and c==n-1: return t
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                visited.add((nr,nc))
                heapq.heappush(heap,(max(t,grid[nr][nc]),nr,nc))
    return -1
if __name__=="__main__":
    cases=[([[0,2],[1,3]],3),([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]],16)]
    for grid,expected in cases:
        result=swim_in_water(grid)
        print(f"Result={result} {'✓' if result==expected else '✗'}")
