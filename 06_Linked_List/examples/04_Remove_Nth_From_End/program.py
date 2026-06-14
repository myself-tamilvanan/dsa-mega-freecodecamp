"""LC 19 - Remove Nth Node From End"""
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
def remove_nth(head, n):
    dummy=ListNode(0,head);fast=slow=dummy
    for _ in range(n+1): fast=fast.next
    while fast: slow=slow.next;fast=fast.next
    slow.next=slow.next.next
    return dummy.next
if __name__=="__main__":
    for vals,n in [([1,2,3,4,5],2),([1],1),([1,2],1)]:
        print(f"{make(vals)}, n={n} -> {remove_nth(make(vals),n)}")
