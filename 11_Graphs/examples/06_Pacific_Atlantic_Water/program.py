"""LC 417 - Pacific Atlantic Water Flow"""
from collections import deque

def pacific_atlantic(heights):
    rows, cols = len(heights), len(heights[0])
    def bfs(starts):
        q = deque(starts); visited = set(starts)
        while q:
            r,c = q.popleft()
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc = r+dr, c+dc
                if (0<=nr<rows and 0<=nc<cols and
                    (nr,nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    visited.add((nr,nc)); q.append((nr,nc))
        return visited
    pacific = [(0,c) for c in range(cols)] + [(r,0) for r in range(1,rows)]
    atlantic = [(rows-1,c) for c in range(cols)] + [(r,cols-1) for r in range(rows-1)]
    p_reach = bfs(pacific)
    a_reach = bfs(atlantic)
    return [[r,c] for r,c in p_reach & a_reach]

if __name__ == "__main__":
    h = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = pacific_atlantic(h)
    print(f"Cells reachable to both oceans: {result}")
    print(f"Count: {len(result)}")
