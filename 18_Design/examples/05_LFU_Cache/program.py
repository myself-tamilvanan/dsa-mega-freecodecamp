"""LC 460 - LFU Cache"""
from collections import defaultdict,OrderedDict
class LFUCache:
    def __init__(self,cap):
        self.cap=cap;self.min_freq=0
        self.kv={};self.kf={};self.fk=defaultdict(OrderedDict)
    def _update(self,k):
        f=self.kf[k];self.kf[k]=f+1
        del self.fk[f][k]
        if not self.fk[f] and f==self.min_freq: self.min_freq+=1
        self.fk[f+1][k]=None
    def get(self,k):
        if k not in self.kv: return -1
        self._update(k);return self.kv[k]
    def put(self,k,v):
        if self.cap<=0: return
        if k in self.kv: self.kv[k]=v;self._update(k);return
        if len(self.kv)>=self.cap:
            ek,_=self.fk[self.min_freq].popitem(last=False)
            del self.kv[ek];del self.kf[ek]
        self.kv[k]=v;self.kf[k]=1;self.fk[1][k]=None;self.min_freq=1
if __name__=="__main__":
    lfu=LFUCache(2)
    lfu.put(1,1);lfu.put(2,2)
    print(lfu.get(1))   # 1
    lfu.put(3,3)        # evicts key 2
    print(lfu.get(2))   # -1
    print(lfu.get(3))   # 3
    lfu.put(4,4)        # evicts key 1 (freq 1 is min, LRU)
    print(lfu.get(1))   # -1
    print(lfu.get(3))   # 3
    print(lfu.get(4))   # 4
