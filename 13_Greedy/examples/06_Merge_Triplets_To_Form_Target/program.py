from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                result = [max(result[i], t[i]) for i in range(3)]
        return result == list(target)

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))  # True
    print(sol.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))           # False
    print(sol.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))  # True
