# Example 02: Design Twitter (LC 355)

## Problem
Design simplified Twitter:
- postTweet(userId, tweetId)
- getNewsFeed(userId) → 10 most recent tweets from self + followees
- follow(followerId, followeeId)
- unfollow(followerId, followeeId)

## Approach
Heap merge on per-user deques of (timestamp, tweetId).
**Time: O(n log k) getNewsFeed  Space: O(n)**