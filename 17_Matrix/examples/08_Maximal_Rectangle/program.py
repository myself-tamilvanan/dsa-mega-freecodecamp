from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(heights[:]))
        return max_area
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        return max_area

if __name__ == "__main__":
    sol = Solution()
    m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(sol.maximalRectangle(m))  # 6
    print(sol.maximalRectangle([["0"]]))  # 0
    print(sol.maximalRectangle([["1"]]))  # 1
