"""LC 23 - Merge K Sorted Lists"""
import heapq

class ListNode:
    def __init__(self,v=0,n=None): self.val=v;self.next=n
    def __lt__(self,other): return self.val < other.val
    def __repr__(self):
        v,c=[],self
        while c: v.append(str(c.val));c=c.next
        return '->'.join(v)
def make(vals):
    d=ListNode();c=d
    for v in vals: c.next=ListNode(v);c=c.next
    return d.next

def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node: heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode(); curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node; curr = curr.next
        if node.next: heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

if __name__ == "__main__":
    cases = [[[1,4,5],[1,3,4],[2,6]],[[]],[[1]]]
    for lists in cases:
        nodes = [make(l) for l in lists]
        print(f"{lists} -> {merge_k_lists(nodes)}")
