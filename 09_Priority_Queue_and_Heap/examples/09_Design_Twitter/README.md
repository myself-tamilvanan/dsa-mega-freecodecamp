# Design Twitter (LeetCode #355)

## Problem
Design a Twitter-like system that supports:
- postTweet(userId, tweetId): post a tweet
- getNewsFeed(userId): return 10 most recent tweets from user and followed users
- follow(followerId, followeeId): user follows another
- unfollow(followerId, followeeId): user unfollows another

## Examples
Input: ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
       [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
Output: [null,null,[5],null,null,[6,5],null,[5]]

## Approach
HashMap for follows (set), list for tweets (with timestamp). getNewsFeed uses max-heap over all users' tweet lists.

## Complexity
- postTweet: O(1), getNewsFeed: O(N log 10), follow/unfollow: O(1)
