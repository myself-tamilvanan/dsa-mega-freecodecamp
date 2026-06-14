"""LC 33 - Search in Rotated Sorted Array"""
def search(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m]==target: return m
        if nums[l]<=nums[m]:  # left half sorted
            if nums[l]<=target<nums[m]: r=m-1
            else: l=m+1
        else:  # right half sorted
            if nums[m]<target<=nums[r]: l=m+1
            else: r=m-1
    return -1

if __name__=="__main__":
    cases=[([4,5,6,7,0,1,2],0),([4,5,6,7,0,1,2],3),([1],0)]
    for nums,t in cases:
        print(f"{nums}, target={t} -> {search(nums,t)}")
