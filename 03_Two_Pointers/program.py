"""Chapter 03: Two Pointers"""

def is_palindrome(s):
    l,r=0,len(s)-1
    while l<r:
        while l<r and not s[l].isalnum(): l+=1
        while l<r and not s[r].isalnum(): r-=1
        if s[l].lower()!=s[r].lower(): return False
        l+=1;r-=1
    return True

def two_sum_sorted(nums,target):
    l,r=0,len(nums)-1
    while l<r:
        s=nums[l]+nums[r]
        if s==target: return [l+1,r+1]
        elif s<target: l+=1
        else: r-=1

def three_sum(nums):
    nums.sort(); res=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]: continue
        l,r=i+1,len(nums)-1
        while l<r:
            s=nums[i]+nums[l]+nums[r]
            if s==0:
                res.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]: l+=1
                while l<r and nums[r]==nums[r-1]: r-=1
                l+=1;r-=1
            elif s<0: l+=1
            else: r-=1
    return res

def max_area(h):
    l,r=0,len(h)-1; res=0
    while l<r:
        res=max(res,(r-l)*min(h[l],h[r]))
        if h[l]<h[r]: l+=1
        else: r-=1
    return res

def trap(h):
    l,r=0,len(h)-1; lm=rm=water=0
    while l<r:
        if h[l]<h[r]:
            if h[l]>=lm: lm=h[l]
            else: water+=lm-h[l]
            l+=1
        else:
            if h[r]>=rm: rm=h[r]
            else: water+=rm-h[r]
            r-=1
    return water

if __name__=="__main__":
    print("Palindrome:", is_palindrome("A man a plan a canal Panama"))
    print("Two Sum II:", two_sum_sorted([2,7,11,15],9))
    print("3Sum:", three_sum([-1,0,1,2,-1,-4]))
    print("Container:", max_area([1,8,6,2,5,4,8,3,7]))
    print("Trapping Rain Water:", trap([0,1,0,2,1,0,1,3,2,1,2,1]))
