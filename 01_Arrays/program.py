"""Chapter 01: Arrays — Core Patterns"""
from collections import defaultdict, Counter
import heapq

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target-n in seen: return [seen[target-n], i]
        seen[n] = i

def group_anagrams(strs):
    g = defaultdict(list)
    for s in strs: g[tuple(sorted(s))].append(s)
    return list(g.values())

def product_except_self(nums):
    n = len(nums); res = [1]*n
    pre = 1
    for i in range(n): res[i] = pre; pre *= nums[i]
    suf = 1
    for i in range(n-1,-1,-1): res[i] *= suf; suf *= nums[i]
    return res

def top_k_frequent(nums, k):
    return heapq.nlargest(k, Counter(nums), key=Counter(nums).get)

def longest_consecutive(nums):
    s = set(nums); best = 0
    for n in s:
        if n-1 not in s:
            cur = n; streak = 1
            while cur+1 in s: cur+=1; streak+=1
            best = max(best, streak)
    return best

def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
    for i in range(n):
        if nums[i]!=i+1: return i+1
    return n+1

if __name__=="__main__":
    print("Two Sum:", two_sum([2,7,11,15],9))
    print("Group Anagrams:", group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print("Product Except Self:", product_except_self([1,2,3,4]))
    print("Top 2 Frequent:", top_k_frequent([1,1,1,2,2,3],2))
    print("Longest Consecutive:", longest_consecutive([100,4,200,1,3,2]))
    print("First Missing Positive:", first_missing_positive([3,4,-1,1]))
