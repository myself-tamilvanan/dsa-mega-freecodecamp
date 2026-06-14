"""LC 706 - Design HashMap"""

class MyHashMap:
    def __init__(self):
        self.size = 1009  # prime to reduce collisions
        self.buckets = [[] for _ in range(self.size)]

    def _idx(self, key): return key % self.size

    def put(self, key, value):
        bucket = self.buckets[self._idx(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key: bucket[i] = (key, value); return
        bucket.append((key, value))

    def get(self, key):
        for k, v in self.buckets[self._idx(key)]:
            if k == key: return v
        return -1

    def remove(self, key):
        idx = self._idx(key)
        self.buckets[idx] = [(k,v) for k,v in self.buckets[idx] if k!=key]

if __name__ == "__main__":
    hm = MyHashMap()
    ops = [("put",1,1),("put",2,2),("get",1),("get",3),("put",2,1),
           ("get",2),("remove",2),("get",2)]
    for op in ops:
        if op[0]=="put": hm.put(op[1],op[2]); print(f"put({op[1]},{op[2]})")
        elif op[0]=="get": print(f"get({op[1]}) = {hm.get(op[1])}")
        else: hm.remove(op[1]); print(f"remove({op[1]})")
