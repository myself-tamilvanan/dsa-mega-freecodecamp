"""LC 26 - Remove Duplicates From Sorted Array"""
def remove_duplicates(nums):
    if not nums: return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

def remove_duplicates_ii(nums):
    """LC 80 - Allow at most 2 duplicates"""
    if len(nums) <= 2: return len(nums)
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

if __name__ == "__main__":
    cases = [[1,1,2],[0,0,1,1,1,2,2,3,3,4],[1,2,3]]
    for nums in cases:
        arr = nums[:]
        k = remove_duplicates(arr)
        print(f"{nums} -> k={k}, nums={arr[:k]}")
    print("\nAllow 2 duplicates:")
    for nums in [[1,1,1,2,2,3],[0,0,1,1,1,1,2,3,3]]:
        arr = nums[:]
        k = remove_duplicates_ii(arr)
        print(f"{nums} -> k={k}, nums={arr[:k]}")
