"""LC 230 - Kth Smallest Element in BST"""
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
def kth_smallest(root,k):
    stack=[]; curr=root
    count=0
    while stack or curr:
        while curr: stack.append(curr);curr=curr.left
        curr=stack.pop();count+=1
        if count==k: return curr.val
        curr=curr.right
if __name__=="__main__":
    cases=[([3,1,4,None,2],1,1),([5,3,6,2,4,None,None,1],3,3)]
    for vals,k,expected in cases:
        result=kth_smallest(build(vals),k)
        print(f"{vals}, k={k} -> {result} {'✓' if result==expected else '✗'}")
