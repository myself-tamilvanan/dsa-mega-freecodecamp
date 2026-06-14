"""Chapter 02: Sliding Window"""
from collections import defaultdict, deque

def max_profit(prices):
    min_p, profit = float('inf'), 0
    for p in prices: min_p=min(min_p,p); profit=max(profit,p-min_p)
    return profit

def check_inclusion(s1, s2):
    need = defaultdict(int)
    for c in s1: need[c]+=1
    win = defaultdict(int); k = len(s1)
    for i,c in enumerate(s2):
        win[c]+=1
        if i>=k: lc=s2[i-k]; win[lc]-=1
        if i>=k-1 and all(win[c]>=need[c] for c in need): return True
    return False

def length_of_longest_substring(s):
    idx={}; l=0; res=0
    for r,c in enumerate(s):
        if c in idx and idx[c]>=l: l=idx[c]+1
        idx[c]=r; res=max(res,r-l+1)
    return res

def character_replacement(s,k):
    cnt=defaultdict(int); l=0; mx=0; res=0
    for r,c in enumerate(s):
        cnt[c]+=1; mx=max(mx,cnt[c])
        while (r-l+1)-mx>k: cnt[s[l]]-=1; l+=1
        res=max(res,r-l+1)
    return res

def max_sliding_window(nums,k):
    dq=deque(); res=[]
    for i,n in enumerate(nums):
        while dq and dq[0]<i-k+1: dq.popleft()
        while dq and nums[dq[-1]]<n: dq.pop()
        dq.append(i)
        if i>=k-1: res.append(nums[dq[0]])
    return res

if __name__=="__main__":
    print("Max Profit:", max_profit([7,1,5,3,6,4]))
    print("Permutation in String:", check_inclusion("ab","eidbaooo"))
    print("Longest Substring:", length_of_longest_substring("abcabcbb"))
    print("Char Replacement:", character_replacement("AABABBA",1))
    print("Sliding Window Max:", max_sliding_window([1,3,-1,-3,5,3,6,7],3))
