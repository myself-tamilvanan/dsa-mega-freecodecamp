from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    n5 = TreeNode(5); n1 = TreeNode(1)
    root.left = n5; root.right = n1
    n5.left = TreeNode(6); n5.right = TreeNode(2, TreeNode(7), TreeNode(4))
    n1.left = TreeNode(0); n1.right = TreeNode(8)
    lca = sol.lowestCommonAncestor(root, n5, n1)
    print(lca.val)  # 3
    n4 = TreeNode(4)
    n5.right.right = n4
    lca2 = sol.lowestCommonAncestor(root, n5, n4)
    print(lca2.val)  # 5
