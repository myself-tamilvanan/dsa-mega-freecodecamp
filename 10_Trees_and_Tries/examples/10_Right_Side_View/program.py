"""LC 199 - Binary Tree Right Side View"""
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
def right_side_view(root):
    if not root: return []
    result=[];q=deque([root])
    while q:
        level_size=len(q)
        for i in range(level_size):
            node=q.popleft()
            if i==level_size-1: result.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return result
if __name__=="__main__":
    cases=[[1,2,3,None,5,None,4],[1,None,3],[],  [1,2,3,4,None,None,None,5]]
    for vals in cases:
        print(f"{vals} -> {right_side_view(build(vals))}")
