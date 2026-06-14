from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        cur_max = cur_min = 1
        for n in nums:
            if n == 0:
                cur_max = cur_min = 1
                continue
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            result = max(result, cur_max)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))   # 6
    print(sol.maxProduct([-2,0,-1]))     # 0
    print(sol.maxProduct([-2,3,-4]))     # 24
