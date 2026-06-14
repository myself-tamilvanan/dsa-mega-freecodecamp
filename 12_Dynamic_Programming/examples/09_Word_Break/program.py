from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet","code"]))             # True
    print(sol.wordBreak("applepenapple", ["apple","pen"]))        # True
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # False
