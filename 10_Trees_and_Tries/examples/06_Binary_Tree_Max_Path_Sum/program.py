"""LC 124 - Binary Tree Maximum Path Sum"""
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

def max_path_sum(root):
    result = [float('-inf')]
    def dfs(node):
        if not node: return 0
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)
        # Best path through this node
        result[0] = max(result[0], node.val + left_gain + right_gain)
        # Return best single-branch contribution
        return node.val + max(left_gain, right_gain)
    dfs(root)
    return result[0]

if __name__ == "__main__":
    trees = [[-10,9,20,None,None,15,7],[1,2,3],[-3],[-1,-2,-3]]
    for vals in trees:
        t=build(vals)
        print(f"{vals} -> max path sum = {max_path_sum(t)}")
