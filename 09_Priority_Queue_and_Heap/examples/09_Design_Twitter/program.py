import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> [(timestamp, tweetId)]
        self.following = defaultdict(set) # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        heap = []
        users = self.following[userId] | {userId}
        for uid in users:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                t, tid = tweets[idx]
                heapq.heappush(heap, (-t, tid, uid, idx - 1))
        result = []
        while heap and len(result) < 10:
            neg_t, tid, uid, next_idx = heapq.heappop(heap)
            result.append(tid)
            if next_idx >= 0:
                t, tid2 = self.tweets[uid][next_idx]
                heapq.heappush(heap, (-t, tid2, uid, next_idx - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print(tw.getNewsFeed(1))   # [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print(tw.getNewsFeed(1))   # [6, 5]
    tw.unfollow(1, 2)
    print(tw.getNewsFeed(1))   # [5]
