"""Chapter 12: Dynamic Programming"""
from functools import lru_cache
import bisect

def climb_stairs(n):
    a,b=1,2
    for _ in range(3,n+1): a,b=b,a+b
    return b if n>=2 else n

def coin_change(coins,amount):
    dp=[float('inf')]*(amount+1);dp[0]=0
    for amt in range(1,amount+1):
        for c in coins:
            if c<=amt: dp[amt]=min(dp[amt],dp[amt-c]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

def rob(nums):
    p2=p1=0
    for n in nums: p2,p1=p1,max(p1,p2+n)
    return p1

def length_of_lis(nums):
    tails=[]
    for n in nums:
        i=bisect.bisect_left(tails,n)
        if i==len(tails): tails.append(n)
        else: tails[i]=n
    return len(tails)

def lcs(t1,t2):
    m,n=len(t1),len(t2);dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1]+1 if t1[i-1]==t2[j-1] else max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

def edit_distance(w1,w2):
    m,n=len(w1),len(w2);dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=i
    for j in range(n+1): dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1] if w1[i-1]==w2[j-1] else 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]

def can_partition(nums):
    t=sum(nums)
    if t%2: return False
    dp={0}
    for n in nums: dp|={s+n for s in dp if s+n<=t//2}
    return t//2 in dp

if __name__=="__main__":
    print("Climb Stairs(10):", climb_stairs(10))
    print("Coin Change [1,5,11],15:", coin_change([1,5,11],15))
    print("House Robber [1,2,3,1]:", rob([1,2,3,1]))
    print("LIS [10,9,2,5,3,7,101]:", length_of_lis([10,9,2,5,3,7,101]))
    print("LCS 'abcde','ace':", lcs("abcde","ace"))
    print("Edit Distance 'horse','ros':", edit_distance("horse","ros"))
    print("Can Partition [1,5,11,5]:", can_partition([1,5,11,5]))
