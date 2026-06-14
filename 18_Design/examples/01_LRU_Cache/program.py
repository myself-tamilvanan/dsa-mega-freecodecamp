"""LC 146 - LRU Cache"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key)  # most recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # remove LRU

if __name__ == "__main__":
    lru = LRUCache(2)
    ops = [('put',1,1),('put',2,2),('get',1,None),('put',3,3),
           ('get',2,None),('put',4,4),('get',1,None),('get',3,None),('get',4,None)]
    for op in ops:
        if op[0]=='put':
            lru.put(op[1],op[2])
            print(f"put({op[1]},{op[2]})")
        else:
            result=lru.get(op[1])
            print(f"get({op[1]}) = {result}")
