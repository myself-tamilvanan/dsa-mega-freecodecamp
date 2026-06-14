"""LC 98 - Validate Binary Search Tree"""
from collections import deque

class TreeNode:
    def __init__(self,v=0,l=None,r=None): self.val=v;self.left=l;self.right=r

def build(vals):
    if not vals: return None
    root=TreeNode(vals[0]);q=deque([root]);i=1
    while q and i<len(vals):
        n=q.popleft()
        if i<len(vals) and vals[i] is not None: n.left=TreeNode(vals[i]);q.append(n.left)
        i+=1
        if i<len(vals) and vals[i] is not None: n.right=TreeNode(vals[i]);q.append(n.right)
        i+=1
    return root

def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if not (lo < root.val < hi): return False
    return is_valid_bst(root.left, lo, root.val) and is_valid_bst(root.right, root.val, hi)

def is_valid_bst_inorder(root):
    """Inorder traversal must be strictly increasing"""
    prev = [float('-inf')]
    def inorder(node):
        if not node: return True
        if not inorder(node.left): return False
        if node.val <= prev[0]: return False
        prev[0] = node.val
        return inorder(node.right)
    return inorder(root)

if __name__ == "__main__":
    trees = [[2,1,3],[5,1,4,None,None,3,6],[2,2,2]]
    for vals in trees:
        t=build(vals)
        print(f"{vals} -> bounds={is_valid_bst(t)}, inorder={is_valid_bst_inorder(t)}")
