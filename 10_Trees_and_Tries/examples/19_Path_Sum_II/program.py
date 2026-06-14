from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, remaining, path):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                result.append(list(path))
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)
            path.pop()
        
        dfs(root, targetSum, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    # Build: [5,4,8,11,null,13,4,7,2,null,null,5,1]
    root = TreeNode(5)
    root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None)
    root.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
    print(sol.pathSum(root, 22))  # [[5,4,11,2],[5,8,4,5]]
    print(sol.pathSum(None, 0))   # []
