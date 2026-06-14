"""LC 2 - Add Two Numbers"""
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
def add_two_numbers(l1,l2):
    dummy=ListNode();curr=dummy;carry=0
    while l1 or l2 or carry:
        v1=l1.val if l1 else 0
        v2=l2.val if l2 else 0
        total=v1+v2+carry;carry=total//10
        curr.next=ListNode(total%10);curr=curr.next
        if l1: l1=l1.next
        if l2: l2=l2.next
    return dummy.next
if __name__=="__main__":
    cases=[([2,4,3],[5,6,4]),([0],[0]),([9,9,9,9,9,9,9],[9,9,9,9])]
    for a,b in cases:
        print(f"{make(a)} + {make(b)} = {add_two_numbers(make(a),make(b))}")
