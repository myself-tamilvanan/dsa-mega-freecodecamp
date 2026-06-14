"""Chapter 10: Trees & Tries"""
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

def max_depth(r): return 0 if not r else 1+max(max_depth(r.left),max_depth(r.right))
def invert(r):
    if r: r.left,r.right=invert(r.right),invert(r.left)
    return r
def level_order(r):
    if not r: return []
    res=[];q=deque([r])
    while q:
        lv=[]
        for _ in range(len(q)):
            n=q.popleft();lv.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        res.append(lv)
    return res
def is_valid_bst(r,lo=float('-inf'),hi=float('inf')):
    if not r: return True
    return lo<r.val<hi and is_valid_bst(r.left,lo,r.val) and is_valid_bst(r.right,r.val,hi)
def diameter(root):
    res=[0]
    def depth(n):
        if not n: return 0
        l,r=depth(n.left),depth(n.right);res[0]=max(res[0],l+r)
        return 1+max(l,r)
    depth(root);return res[0]

class TrieNode:
    def __init__(self): self.ch={};self.end=False
class Trie:
    def __init__(self): self.root=TrieNode()
    def insert(self,w):
        n=self.root
        for c in w: n.ch.setdefault(c,TrieNode());n=n.ch[c]
        n.end=True
    def search(self,w):
        n=self.root
        for c in w:
            if c not in n.ch: return False
            n=n.ch[c]
        return n.end
    def starts_with(self,p):
        n=self.root
        for c in p:
            if c not in n.ch: return False
            n=n.ch[c]
        return True

if __name__=="__main__":
    t=build([1,2,3,4,5,None,6])
    print("Max Depth:", max_depth(t))
    print("Level Order:", level_order(t))
    print("Diameter:", diameter(t))
    bst=build([5,3,7,2,4,6,8])
    print("Valid BST:", is_valid_bst(bst))
    trie=Trie();[trie.insert(w) for w in ["apple","app","apricot"]]
    print("Trie search 'apple':", trie.search("apple"), "search 'ap':", trie.search("ap"))
