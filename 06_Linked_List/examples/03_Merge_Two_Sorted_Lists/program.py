"""LC 21 - Merge Two Sorted Lists"""
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
def merge_two_lists(l1,l2):
    dummy=ListNode();curr=dummy
    while l1 and l2:
        if l1.val<=l2.val: curr.next=l1;l1=l1.next
        else: curr.next=l2;l2=l2.next
        curr=curr.next
    curr.next=l1 or l2
    return dummy.next
if __name__=="__main__":
    cases=[([1,2,4],[1,3,4]),([],[]),([],[0])]
    for a,b in cases:
        print(f"{make(a)} + {make(b)} -> {merge_two_lists(make(a),make(b))}")
