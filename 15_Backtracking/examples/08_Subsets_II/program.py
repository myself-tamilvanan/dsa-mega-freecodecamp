from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(start, path):
            result.append(list(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(sol.subsetsWithDup([0]))      # [[],[0]]
