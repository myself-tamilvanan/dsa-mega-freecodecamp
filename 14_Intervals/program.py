"""Chapter 14: Intervals"""
import heapq

def merge(intervals):
    intervals.sort();res=[intervals[0]]
    for s,e in intervals[1:]:
        if s<=res[-1][1]: res[-1][1]=max(res[-1][1],e)
        else: res.append([s,e])
    return res

def insert(intervals,new):
    res=[];i=0;n=len(intervals)
    while i<n and intervals[i][1]<new[0]: res.append(intervals[i]);i+=1
    while i<n and intervals[i][0]<=new[1]:
        new[0]=min(new[0],intervals[i][0]);new[1]=max(new[1],intervals[i][1]);i+=1
    res.append(new);res.extend(intervals[i:])
    return res

def erase_overlap(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x:x[1]);rm=0;end=intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0]<end: rm+=1
        else: end=intervals[i][1]
    return rm

def min_rooms(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x:x[0]);h=[]
    for s,e in intervals:
        if h and h[0]<=s: heapq.heapreplace(h,e)
        else: heapq.heappush(h,e)
    return len(h)

if __name__=="__main__":
    print("Merge:", merge([[1,3],[2,6],[8,10],[15,18]]))
    print("Insert:", insert([[1,3],[6,9]],[2,5]))
    print("Erase Overlap:", erase_overlap([[1,2],[2,3],[3,4],[1,3]]))
    print("Min Rooms:", min_rooms([[0,30],[5,10],[15,20]]))
