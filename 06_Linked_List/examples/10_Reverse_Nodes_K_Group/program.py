"""LC 25 - Reverse Nodes in K-Group"""
class ListNode:
    def __init__(self,v=0,n=None): self.val=v;self.next=n
    def __repr__(self):
        v,c=[],self
        while c: v.append(str(c.val));c=c.next
        return '->'.join(v)
def make(vals):
    d=ListNode();c=d
    for v in vals: c.next=ListNode(v);c=c.next
    return d.next

def reverse_k_group(head, k):
    # Check if k nodes remain
    node, count = head, 0
    while node and count < k: node=node.next;count+=1
    if count < k: return head
    # Reverse k nodes
    prev, curr = None, head
    for _ in range(k):
        nxt=curr.next;curr.next=prev;prev=curr;curr=nxt
    # head is now tail; connect to recursively reversed rest
    head.next = reverse_k_group(curr, k)
    return prev

if __name__ == "__main__":
    cases = [([1,2,3,4,5],2),([1,2,3,4,5],3),([1,2,3,4,5],1),([1],2)]
    for vals,k in cases:
        print(f"{vals}, k={k} -> {reverse_k_group(make(vals), k)}")
