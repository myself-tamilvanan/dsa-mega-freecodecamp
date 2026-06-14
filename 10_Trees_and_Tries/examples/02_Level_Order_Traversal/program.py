"""LC 102 - Binary Tree Level Order Traversal"""
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

def level_order(root):
    if not root: return []
    result=[]; q=deque([root])
    while q:
        level=[]
        for _ in range(len(q)):
            node=q.popleft(); level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result

def zigzag_level_order(root):
    """LC 103 - Zigzag variant"""
    if not root: return []
    result=[]; q=deque([root]); left_to_right=True
    while q:
        level=[]
        for _ in range(len(q)):
            node=q.popleft(); level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level if left_to_right else level[::-1])
        left_to_right=not left_to_right
    return result

if __name__ == "__main__":
    t=build([3,9,20,None,None,15,7])
    print("Level Order:", level_order(t))
    print("Zigzag Order:", zigzag_level_order(t))
    t2=build([1,2,3,4,5])
    print("Level Order [1,2,3,4,5]:", level_order(t2))
