"""LC 101 - Symmetric Tree"""
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
def is_symmetric(root):
    def mirror(l,r):
        if not l and not r: return True
        if not l or not r: return False
        return l.val==r.val and mirror(l.left,r.right) and mirror(l.right,r.left)
    return mirror(root.left,root.right) if root else True
if __name__=="__main__":
    cases=[([1,2,2,3,4,4,3],True),([1,2,2,None,3,None,3],False),([1],True)]
    for vals,expected in cases:
        result=is_symmetric(build(vals))
        print(f"{vals} -> {result} {'✓' if result==expected else '✗'}")
