from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def height(node):
            if not node:
                return -1
            h = 1 + max(height(node.left), height(node.right))
            if h == len(result):
                result.append([])
            result[h].append(node.val)
            return h
        height(root)
        return result

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(sol.findLeaves(root))  # [[4,5,3],[2],[1]]
    print(sol.findLeaves(TreeNode(1)))  # [[1]]
