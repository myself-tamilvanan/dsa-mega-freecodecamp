"""LC 704 - Binary Search"""
def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m]==target: return m
        elif nums[m]<target: l=m+1
        else: r=m-1
    return -1

if __name__=="__main__":
    cases=[([-1,0,3,5,9,12],9),([-1,0,3,5,9,12],2),([5],5),([5],3)]
    for nums,t in cases:
        print(f"{nums}, target={t} -> {search(nums,t)}")
