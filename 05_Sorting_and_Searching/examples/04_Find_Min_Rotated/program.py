"""LC 153 - Find Minimum in Rotated Sorted Array"""
def find_min(nums):
    l, r = 0, len(nums)-1
    while l < r:
        m = (l+r)//2
        if nums[m] > nums[r]: l=m+1  # min is in right half
        else: r=m  # min is in left half (including mid)
    return nums[l]

if __name__=="__main__":
    cases=[[3,4,5,1,2],[4,5,6,7,0,1,2],[11,13,15,17],[1]]
    for nums in cases:
        print(f"{nums} -> min={find_min(nums)}")
