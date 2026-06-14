"""LC 684 - Redundant Connection"""
def find_redundant_connection(edges):
    parent=list(range(len(edges)+1))
    def find(x):
        if parent[x]!=x: parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        px,py=find(x),find(y)
        if px==py: return False
        parent[px]=py; return True
    for u,v in edges:
        if not union(u,v): return [u,v]
if __name__=="__main__":
    cases=[([[1,2],[1,3],[2,3]],[2,3]),([[1,2],[2,3],[3,4],[1,4],[1,5]],[1,4])]
    for edges,expected in cases:
        result=find_redundant_connection(edges)
        print(f"{edges} -> {result} {'✓' if result==expected else '✗'}")
