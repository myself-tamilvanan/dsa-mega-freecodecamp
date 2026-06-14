"""LC 572 - Subtree of Another Tree"""
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
def is_same(s,t):
    if not s and not t: return True
    if not s or not t: return False
    return s.val==t.val and is_same(s.left,t.left) and is_same(s.right,t.right)
def is_subtree(root,subRoot):
    if not root: return False
    if is_same(root,subRoot): return True
    return is_subtree(root.left,subRoot) or is_subtree(root.right,subRoot)
if __name__=="__main__":
    cases=[([3,4,5,1,2],[4,1,2],True),([3,4,5,1,2,None,None,None,None,0],[4,1,2],False)]
    for r,s,expected in cases:
        result=is_subtree(build(r),build(s))
        print(f"root={r}, sub={s} -> {result} {'✓' if result==expected else '✗'}")
