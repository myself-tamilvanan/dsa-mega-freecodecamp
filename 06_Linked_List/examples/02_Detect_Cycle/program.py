"""LC 141 - Linked List Cycle"""
class ListNode:
    def __init__(self,v=0,n=None): self.val=v;self.next=n
def has_cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next;fast=fast.next.next
        if slow==fast: return True
    return False
def make_with_cycle(vals, pos):
    if not vals: return None
    nodes=[ListNode(v) for v in vals]
    for i in range(len(nodes)-1): nodes[i].next=nodes[i+1]
    if pos>=0: nodes[-1].next=nodes[pos]
    return nodes[0]
if __name__=="__main__":
    h1=make_with_cycle([3,2,0,-4],1)
    h2=make_with_cycle([1,2],0)
    h3=make_with_cycle([1],-1)
    print("Cycle at pos 1:", has_cycle(h1))
    print("Cycle at pos 0:", has_cycle(h2))
    print("No cycle:", has_cycle(h3))
