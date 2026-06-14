"""LC 543 - Diameter of Binary Tree"""
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

def diameter_of_binary_tree(root):
    result = [0]
    def depth(node):
        if not node: return 0
        l = depth(node.left)
        r = depth(node.right)
        result[0] = max(result[0], l + r)  # path through this node
        return 1 + max(l, r)
    depth(root)
    return result[0]

if __name__ == "__main__":
    trees = [[1,2,3,4,5],[1,2],[1],[3,4,5,1,2,None,None]]
    for vals in trees:
        t=build(vals)
        print(f"{vals} -> diameter={diameter_of_binary_tree(t)}")
