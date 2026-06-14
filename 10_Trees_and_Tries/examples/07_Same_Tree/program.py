"""LC 100 - Same Tree"""
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
def is_same_tree(p,q):
    if not p and not q: return True
    if not p or not q: return False
    return p.val==q.val and is_same_tree(p.left,q.left) and is_same_tree(p.right,q.right)
if __name__=="__main__":
    cases=[([1,2,3],[1,2,3],True),([1,2],[1,None,2],False),([1,2,1],[1,1,2],False)]
    for a,b,expected in cases:
        result=is_same_tree(build(a),build(b))
        print(f"{a} vs {b} -> {result} {'✓' if result==expected else '✗'}")
