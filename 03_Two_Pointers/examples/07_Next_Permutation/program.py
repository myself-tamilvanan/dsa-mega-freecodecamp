"""LC 31 - Next Permutation"""
def next_permutation(nums):
    n = len(nums)
    i = n - 2
    # Step 1: find first decreasing element from right
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        # Step 2: find element just larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    # Step 3: reverse from i+1
    nums[i+1:] = nums[i+1:][::-1]
    return nums

if __name__ == "__main__":
    cases = [[1,2,3],[3,2,1],[1,1,5],[1,3,2],[2,3,1],[1,2,3,4,5]]
    for nums in cases:
        original = nums[:]
        result = next_permutation(nums[:])
        print(f"{original} -> {result}")
