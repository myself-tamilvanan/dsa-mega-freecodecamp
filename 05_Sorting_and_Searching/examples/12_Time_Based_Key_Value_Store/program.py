"""LC 981 - Time Based Key-Value Store"""
import bisect
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store: return ""
        entries = self.store[key]
        # Binary search for largest timestamp <= given
        lo, hi = 0, len(entries)-1
        result = ""
        while lo <= hi:
            mid = (lo+hi)//2
            if entries[mid][0] <= timestamp:
                result = entries[mid][1]
                lo = mid+1
            else:
                hi = mid-1
        return result

if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo","bar",1)
    print(tm.get("foo",1))   # bar
    print(tm.get("foo",3))   # bar
    tm.set("foo","bar2",4)
    print(tm.get("foo",4))   # bar2
    print(tm.get("foo",5))   # bar2
    print(tm.get("foo",0))   # (empty)
