"""LC 235 - LCA of BST"""
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
def lca_bst(root,p,q):
    while root:
        if p < root.val and q < root.val: root=root.left
        elif p > root.val and q > root.val: root=root.right
        else: return root.val
if __name__=="__main__":
    bst=build([6,2,8,0,4,7,9,None,None,3,5])
    cases=[(2,8,6),(2,4,2),(2,0,2)]
    for p,q,expected in cases:
        result=lca_bst(bst,p,q)
        print(f"p={p},q={q} -> LCA={result} {'✓' if result==expected else '✗'}")
