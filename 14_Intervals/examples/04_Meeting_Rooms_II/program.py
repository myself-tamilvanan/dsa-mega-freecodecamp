"""Meeting Rooms I & II"""
import heapq

def can_attend_all(intervals):
    """Meeting Rooms I - can one person attend all?"""
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]: return False
    return True

def min_meeting_rooms(intervals):
    """Meeting Rooms II - min rooms needed"""
    if not intervals: return 0
    intervals.sort(key=lambda x: x[0])
    heap = []  # end times
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)

if __name__ == "__main__":
    cases = [[[0,30],[5,10],[15,20]], [[7,10],[2,4]], [[1,5],[2,6],[3,7]]]
    for intervals in cases:
        print(f"{intervals}")
        print(f"  Can attend all: {can_attend_all(sorted(intervals))}")
        print(f"  Min rooms: {min_meeting_rooms(intervals[:])}")
