"""LC 355 - Design Twitter"""
import heapq
from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(deque)   # userId -> deque of (-time, tweetId)
        self.follows = defaultdict(set)     # userId -> set of followees

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((self.time, tweetId))
        self.time -= 1  # decreasing so min-heap gives latest
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId):
        heap = []
        for uid in self.follows[userId] | {userId}:
            if self.tweets[uid]:
                t, tid = self.tweets[uid][0]
                heapq.heappush(heap, (t, tid, uid, 0))
        feed = []
        while heap and len(feed) < 10:
            t, tid, uid, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx+1 < len(self.tweets[uid]):
                nt, ntid = self.tweets[uid][idx+1]
                heapq.heappush(heap, (nt, ntid, uid, idx+1))
        return feed

    def follow(self, fr, fe): self.follows[fr].add(fe)
    def unfollow(self, fr, fe): self.follows[fr].discard(fe)

if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print("User1 feed:", tw.getNewsFeed(1))
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print("User1 feed after following user2:", tw.getNewsFeed(1))
    tw.unfollow(1, 2)
    print("User1 feed after unfollowing:", tw.getNewsFeed(1))
