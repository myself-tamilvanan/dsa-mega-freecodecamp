"""LC 261 - Graph Valid Tree"""
def valid_tree(n, edges):
    if len(edges) != n-1: return False
    parent=list(range(n))
    def find(x):
        if parent[x]!=x: parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        px,py=find(x),find(y)
        if px==py: return False
        parent[px]=py; return True
    return all(union(u,v) for u,v in edges)
if __name__=="__main__":
    cases=[(5,[[0,1],[0,2],[0,3],[1,4]],True),(5,[[0,1],[1,2],[2,3],[1,3],[1,4]],False),(1,[],True)]
    for n,edges,expected in cases:
        result=valid_tree(n,edges)
        print(f"n={n}, edges={edges} -> {result} {'✓' if result==expected else '✗'}")
