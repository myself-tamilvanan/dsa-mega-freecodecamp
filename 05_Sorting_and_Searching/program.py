"""Chapter 05: Sorting & Searching"""
import math

def binary_search(nums, target):
    l,r=0,len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target: return m
        elif nums[m]<target: l=m+1
        else: r=m-1
    return -1

def search_range(nums, target):
    def bound(find_first):
        l,r,res=0,len(nums)-1,-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                res=m
                if find_first: r=m-1
                else: l=m+1
            elif nums[m]<target: l=m+1
            else: r=m-1
        return res
    return [bound(True),bound(False)]

def sort_colors(nums):
    lo=mi=0; hi=len(nums)-1
    while mi<=hi:
        if nums[mi]==0: nums[lo],nums[mi]=nums[mi],nums[lo];lo+=1;mi+=1
        elif nums[mi]==1: mi+=1
        else: nums[mi],nums[hi]=nums[hi],nums[mi];hi-=1
    return nums

def search_rotated(nums, target):
    l,r=0,len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target: return m
        if nums[l]<=nums[m]:
            if nums[l]<=target<nums[m]: r=m-1
            else: l=m+1
        else:
            if nums[m]<target<=nums[r]: l=m+1
            else: r=m-1
    return -1

def min_eating_speed(piles, h):
    l,r=1,max(piles)
    while l<r:
        m=(l+r)//2
        if sum(math.ceil(p/m) for p in piles)<=h: r=m
        else: l=m+1
    return l

if __name__=="__main__":
    print("Binary Search:", binary_search(list(range(1,11)),7))
    print("Search Range:", search_range([5,7,7,8,8,10],8))
    print("Sort Colors:", sort_colors([2,0,2,1,1,0]))
    print("Search Rotated:", search_rotated([4,5,6,7,0,1,2],0))
    print("Min Eating Speed:", min_eating_speed([3,6,7,11],8))
