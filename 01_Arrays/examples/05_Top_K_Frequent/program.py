"""LC 347 - Top K Frequent Elements"""
import heapq
from collections import Counter

def top_k_frequent_heap(nums, k):
    """Min-heap approach O(n log k)"""
    count = Counter(nums)
    return heapq.nlargest(k, count, key=count.get)

def top_k_frequent_bucket(nums, k):
    """Bucket sort O(n)"""
    count = Counter(nums)
    freq = [[] for _ in range(len(nums)+1)]
    for num, cnt in count.items():
        freq[cnt].append(num)
    result = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result)==k: return result
    return result

if __name__=="__main__":
    cases = [([1,1,1,2,2,3],2),([1],1),([1,2],2)]
    for nums,k in cases:
        print(f"Heap: {top_k_frequent_heap(nums,k)}, Bucket: {top_k_frequent_bucket(nums,k)}")
