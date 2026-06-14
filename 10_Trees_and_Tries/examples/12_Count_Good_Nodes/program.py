"""LC 1448 - Count Good Nodes"""
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
def good_nodes(root):
    def dfs(node,max_so_far):
        if not node: return 0
        count=1 if node.val>=max_so_far else 0
        new_max=max(max_so_far,node.val)
        return count+dfs(node.left,new_max)+dfs(node.right,new_max)
    return dfs(root,root.val) if root else 0
if __name__=="__main__":
    cases=[([3,1,4,3,None,1,5],4),([3,3,None,4,2],3),([1],1)]
    for vals,expected in cases:
        result=good_nodes(build(vals))
        print(f"{vals} -> {result} {'✓' if result==expected else '✗'}")
