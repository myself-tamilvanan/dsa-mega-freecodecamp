"""LC 239 - Sliding Window Maximum"""
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # indices; front = current max
    result = []
    for i, n in enumerate(nums):
        # Remove out-of-window indices
        while dq and dq[0] < i-k+1: dq.popleft()
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < n: dq.pop()
        dq.append(i)
        if i >= k-1: result.append(nums[dq[0]])
    return result

if __name__=="__main__":
    cases = [([1,3,-1,-3,5,3,6,7],3),([1],1),([1,-1],1)]
    for nums,k in cases:
        print(f"{nums}, k={k} -> {max_sliding_window(nums,k)}")
