"""LC 133 - Clone Graph"""
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val; self.neighbors = neighbors or []

def clone_graph(node):
    if not node: return None
    clones = {node: Node(node.val)}
    q = deque([node])
    while q:
        curr = q.popleft()
        for nb in curr.neighbors:
            if nb not in clones:
                clones[nb] = Node(nb.val); q.append(nb)
            clones[curr].neighbors.append(clones[nb])
    return clones[node]

if __name__ == "__main__":
    n1=Node(1); n2=Node(2); n3=Node(3); n4=Node(4)
    n1.neighbors=[n2,n4]; n2.neighbors=[n1,n3]
    n3.neighbors=[n2,n4]; n4.neighbors=[n1,n3]
    cloned = clone_graph(n1)
    print(f"Original node val: {n1.val}, clone val: {cloned.val}")
    print(f"Same object? {n1 is cloned} (should be False)")
    print(f"Clone neighbors: {[n.val for n in cloned.neighbors]}")
    print("Graph cloned successfully!")
