"""LC 1584 - Minimum Cost to Connect All Points (Prim's MST)"""
import heapq

def min_cost_connect_points(points):
    n=len(points)
    visited=set();heap=[(0,0)];total=0
    while len(visited)<n:
        cost,i=heapq.heappop(heap)
        if i in visited: continue
        visited.add(i);total+=cost
        for j in range(n):
            if j not in visited:
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(heap,(dist,j))
    return total
if __name__=="__main__":
    cases=[([[0,0],[2,2],[3,10],[5,2],[7,0]],20),([[3,12],[-2,5],[-4,1]],18),([[0,0]],0)]
    for pts,expected in cases:
        result=min_cost_connect_points(pts)
        print(f"{pts} -> {result} {'✓' if result==expected else '✗'}")
