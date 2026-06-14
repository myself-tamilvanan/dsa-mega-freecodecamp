"""Chapter 09: Priority Queue & Heap"""
import heapq
from collections import Counter, defaultdict, deque

def last_stone_weight(stones):
    h=[-s for s in stones];heapq.heapify(h)
    while len(h)>1:
        y,x=-heapq.heappop(h),-heapq.heappop(h)
        if x!=y: heapq.heappush(h,-(y-x))
    return -h[0] if h else 0

def find_kth_largest(nums,k):
    h=[]
    for n in nums:
        heapq.heappush(h,n)
        if len(h)>k: heapq.heappop(h)
    return h[0]

def k_closest(points,k):
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2+p[1]**2)

def least_interval(tasks,n):
    cnt=Counter(tasks);h=[-c for c in cnt.values()];heapq.heapify(h)
    time=0;q=deque()
    while h or q:
        time+=1
        if h:
            c=1+heapq.heappop(h)
            if c: q.append((c,time+n))
        if q and q[0][1]==time: heapq.heappush(h,q.popleft()[0])
    return time

class MedianFinder:
    def __init__(self): self.small=[];self.large=[]
    def add_num(self,n):
        heapq.heappush(self.small,-n)
        if self.small and self.large and -self.small[0]>self.large[0]:
            heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.small)>len(self.large)+1:
            heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.large)>len(self.small):
            heapq.heappush(self.small,-heapq.heappop(self.large))
    def find_median(self):
        if len(self.small)>len(self.large): return -self.small[0]
        return(-self.small[0]+self.large[0])/2

if __name__=="__main__":
    print("Last Stone:", last_stone_weight([2,7,4,1,8,1]))
    print("Kth Largest:", find_kth_largest([3,2,1,5,6,4],2))
    print("K Closest:", k_closest([[1,3],[-2,2]],1))
    print("Task Scheduler:", least_interval(["A","A","A","B","B","B"],2))
    mf=MedianFinder();[mf.add_num(i) for i in [1,2,3]];print("Median:",mf.find_median())
