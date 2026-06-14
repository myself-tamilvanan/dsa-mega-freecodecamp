"""LC 143 - Reorder List"""
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
def reorder_list(head):
    if not head: return
    s=f=head
    while f and f.next: s=s.next;f=f.next.next
    prev=None;cur=s.next;s.next=None
    while cur: tmp=cur.next;cur.next=prev;prev=cur;cur=tmp
    l,r=head,prev
    while r:
        t1,t2=l.next,r.next
        l.next=r;r.next=t1;l=t1;r=t2
    return head
if __name__=="__main__":
    for vals in [[1,2,3,4],[1,2,3,4,5],[1]]:
        h=make(vals)
        print(f"{make(vals)} -> {reorder_list(h)}")
