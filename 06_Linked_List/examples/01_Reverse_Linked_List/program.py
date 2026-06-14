"""LC 206 - Reverse Linked List"""
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
def reverse_list(head):
    prev=None;curr=head
    while curr:
        nxt=curr.next;curr.next=prev;prev=curr;curr=nxt
    return prev
if __name__=="__main__":
    for vals in [[1,2,3,4,5],[1,2],[1],[]]:
        h=make(vals)
        print(f"{h} -> {reverse_list(h)}")
