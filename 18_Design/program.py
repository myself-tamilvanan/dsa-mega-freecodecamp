"""Chapter 18: Design"""
from collections import OrderedDict,defaultdict,deque
import heapq

class LRUCache:
    def __init__(self,cap): self.cap=cap;self.cache=OrderedDict()
    def get(self,k):
        if k not in self.cache: return -1
        self.cache.move_to_end(k);return self.cache[k]
    def put(self,k,v):
        if k in self.cache: self.cache.move_to_end(k)
        self.cache[k]=v
        if len(self.cache)>self.cap: self.cache.popitem(last=False)

class Twitter:
    def __init__(self): self.t=0;self.tweets=defaultdict(deque);self.follows=defaultdict(set)
    def post_tweet(self,uid,tid):
        self.tweets[uid].appendleft((self.t,tid));self.t-=1
        if len(self.tweets[uid])>10: self.tweets[uid].pop()
    def get_news_feed(self,uid):
        h=[];[heapq.heappush(h,(self.tweets[u][0][0],self.tweets[u][0][1],u,0)) for u in self.follows[uid]|{uid} if self.tweets[u]]
        feed=[]
        while h and len(feed)<10:
            t,tid,u,i=heapq.heappop(h);feed.append(tid)
            if i+1<len(self.tweets[u]): nt,ntid=self.tweets[u][i+1];heapq.heappush(h,(nt,ntid,u,i+1))
        return feed
    def follow(self,fr,fe): self.follows[fr].add(fe)
    def unfollow(self,fr,fe): self.follows[fr].discard(fe)

if __name__=="__main__":
    lru=LRUCache(2);lru.put(1,1);lru.put(2,2)
    print("LRU get(1):", lru.get(1))
    lru.put(3,3);print("LRU get(2) evicted:", lru.get(2))
    tw=Twitter();tw.post_tweet(1,5);print("Feed:", tw.get_news_feed(1))
    tw.follow(1,2);tw.post_tweet(2,6);print("Feed after follow:", tw.get_news_feed(1))
