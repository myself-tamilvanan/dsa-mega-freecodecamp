"""LC 105 - Construct Binary Tree from Preorder and Inorder"""
class TreeNode:
    def __init__(self,v=0,l=None,r=None): self.val=v;self.left=l;self.right=r
    def __repr__(self):
        from collections import deque
        res=[];q=deque([self])
        while q:
            n=q.popleft()
            if n: res.append(n.val);q.append(n.left);q.append(n.right)
            else: res.append(None)
        while res and res[-1] is None: res.pop()
        return str(res)
def build_tree(preorder,inorder):
    if not preorder: return None
    root_val=preorder[0]
    mid=inorder.index(root_val)
    root=TreeNode(root_val)
    root.left=build_tree(preorder[1:mid+1],inorder[:mid])
    root.right=build_tree(preorder[mid+1:],inorder[mid+1:])
    return root
if __name__=="__main__":
    cases=[([3,9,20,15,7],[9,3,15,20,7]),([1],[1]),([1,2],[2,1])]
    for pre,ino in cases:
        tree=build_tree(pre,ino)
        print(f"preorder={pre}, inorder={ino} -> tree={tree}")
