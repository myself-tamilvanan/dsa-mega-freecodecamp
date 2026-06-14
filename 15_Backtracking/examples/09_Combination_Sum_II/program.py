from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(sol.combinationSum2([2,5,2,1,2], 5))         # [[1,2,2],[5]]
