"""LC 215 - Kth Largest Element"""
import heapq, random

def find_kth_largest_heap(nums, k):
    """Min-heap of size k"""
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

def find_kth_largest_quickselect(nums, k):
    """QuickSelect - O(n) average"""
    k = len(nums) - k  # kth largest = (n-k)th smallest
    def quickselect(l, r):
        pivot = nums[r]
        p = l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p == k: return nums[p]
        elif p < k: return quickselect(p+1, r)
        else: return quickselect(l, p-1)
    return quickselect(0, len(nums)-1)

if __name__ == "__main__":
    cases = [([3,2,1,5,6,4],2), ([3,2,3,1,2,4,5,5,6],4)]
    for nums, k in cases:
        h = find_kth_largest_heap(nums[:], k)
        q = find_kth_largest_quickselect(nums[:], k)
        print(f"{nums}, k={k} -> heap={h}, quickselect={q}")
