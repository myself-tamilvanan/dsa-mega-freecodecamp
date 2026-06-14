"""LC 226 - Invert Binary Tree"""
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
def level_vals(root):
    if not root: return []
    res=[];q=deque([root])
    while q:
        n=q.popleft();res.append(n.val)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return res
def invert_tree(root):
    if not root: return None
    root.left,root.right=invert_tree(root.right),invert_tree(root.left)
    return root
if __name__=="__main__":
    for vals in [[4,2,7,1,3,6,9],[2,1,3],[]]:
        t=build(vals)
        print(f"{vals} -> {level_vals(invert_tree(t))}")
