from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = {0}
        for num in nums:
            dp = {s + num for s in dp} | dp
            if target in dp:
                return True
        return target in dp

if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition([1,5,11,5]))  # True
    print(sol.canPartition([1,2,3,5]))   # False
    print(sol.canPartition([2,2,3,5]))   # False
