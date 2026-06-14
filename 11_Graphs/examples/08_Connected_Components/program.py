"""LC 323 - Number of Connected Components"""
def count_components(n, edges):
    parent=list(range(n))
    def find(x):
        if parent[x]!=x: parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        px,py=find(x),find(y)
        if px==py: return 0
        parent[px]=py; return 1
    return n - sum(union(u,v) for u,v in edges)
if __name__=="__main__":
    cases=[(5,[[0,1],[1,2],[3,4]],2),(5,[[0,1],[1,2],[2,3],[3,4]],1),(4,[],4)]
    for n,edges,expected in cases:
        result=count_components(n,edges)
        print(f"n={n}, edges={edges} -> {result} {'✓' if result==expected else '✗'}")
