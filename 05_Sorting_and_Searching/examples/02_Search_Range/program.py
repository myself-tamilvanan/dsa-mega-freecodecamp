"""LC 34 - Find First and Last Position"""
def search_range(nums, target):
    def find(find_first):
        l, r, res = 0, len(nums)-1, -1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                res=m
                if find_first: r=m-1
                else: l=m+1
            elif nums[m]<target: l=m+1
            else: r=m-1
        return res
    return [find(True), find(False)]

if __name__=="__main__":
    cases=[([5,7,7,8,8,10],8),([5,7,7,8,8,10],6),([],0)]
    for nums,t in cases:
        print(f"{nums}, target={t} -> {search_range(nums,t)}")
