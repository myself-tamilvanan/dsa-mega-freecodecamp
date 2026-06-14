"""LC 104 - Maximum Depth of Binary Tree"""
from collections import deque

class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val=v; self.left=l; self.right=r

def build(vals):
    if not vals: return None
    root = TreeNode(vals[0]); q = deque([root]); i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root

def max_depth_dfs(root):
    if not root: return 0
    return 1 + max(max_depth_dfs(root.left), max_depth_dfs(root.right))

def max_depth_bfs(root):
    if not root: return 0
    q = deque([root]); depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return depth

if __name__ == "__main__":
    trees = [[3,9,20,None,None,15,7], [1,None,2], [], [1]]
    for vals in trees:
        t = build(vals)
        print(f"{vals} -> DFS depth={max_depth_dfs(t)}, BFS depth={max_depth_bfs(t)}")
