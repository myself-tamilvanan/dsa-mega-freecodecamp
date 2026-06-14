"""LC 297 - Serialize and Deserialize Binary Tree"""
from collections import deque
class TreeNode:
    def __init__(self,v=0,l=None,r=None): self.val=v;self.left=l;self.right=r
def serialize(root):
    if not root: return "null"
    res=[];q=deque([root])
    while q:
        node=q.popleft()
        if node: res.append(str(node.val));q.append(node.left);q.append(node.right)
        else: res.append("null")
    return ','.join(res)
def deserialize(data):
    if data=="null": return None
    vals=data.split(',')
    root=TreeNode(int(vals[0]))
    q=deque([root]);i=1
    while q and i<len(vals):
        node=q.popleft()
        if i<len(vals) and vals[i]!="null":
            node.left=TreeNode(int(vals[i]));q.append(node.left)
        i+=1
        if i<len(vals) and vals[i]!="null":
            node.right=TreeNode(int(vals[i]));q.append(node.right)
        i+=1
    return root
if __name__=="__main__":
    from collections import deque
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
    trees=[[1,2,3,None,None,4,5],[1],[]]
    for vals in trees:
        t=build(vals)
        s=serialize(t)
        t2=deserialize(s)
        print(f"Original: {vals}\nSerialized: '{s}'\nRe-serialized: '{serialize(t2)}'\nMatch: {serialize(t)==serialize(t2)}\n")
