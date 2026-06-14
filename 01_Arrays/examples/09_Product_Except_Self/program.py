from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        # Left pass: result[i] = product of all nums[0..i-1]
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        # Right pass: multiply by product of nums[i+1..n-1]
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))        # [24,12,8,6]
    print(sol.productExceptSelf([-1,1,0,-3,3]))     # [0,0,9,0,0]
    print(sol.productExceptSelf([2,3]))             # [3,2]
