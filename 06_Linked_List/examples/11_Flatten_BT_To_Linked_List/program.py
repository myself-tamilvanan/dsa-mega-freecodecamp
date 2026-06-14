"""LC 114 - Flatten Binary Tree to Linked List"""
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
def to_list(root):
    res=[]
    while root: res.append(root.val);root=root.right
    return res

def flatten(root):
    curr = root
    while curr:
        if curr.left:
            # Find rightmost of left subtree
            rightmost = curr.left
            while rightmost.right: rightmost = rightmost.right
            # Connect
            rightmost.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right
    return root

if __name__ == "__main__":
    cases = [[1,2,5,3,4,None,6],[1],[1,2,3]]
    for vals in cases:
        t=build(vals)
        flatten(t)
        print(f"{vals} -> {to_list(t)}")
