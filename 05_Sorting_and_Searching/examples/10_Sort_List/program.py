"""LC 148 - Sort List"""
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

def sort_list(head):
    if not head or not head.next: return head
    # Find middle
    slow, fast = head, head.next
    while fast and fast.next: slow=slow.next;fast=fast.next.next
    mid = slow.next; slow.next = None
    # Recurse
    left = sort_list(head)
    right = sort_list(mid)
    # Merge
    dummy = ListNode(); curr = dummy
    while left and right:
        if left.val <= right.val: curr.next=left;left=left.next
        else: curr.next=right;right=right.next
        curr=curr.next
    curr.next = left or right
    return dummy.next

if __name__ == "__main__":
    cases = [[4,2,1,3],[-1,5,3,4,0],[1],[],  [1,1,1]]
    for vals in cases:
        print(f"{vals} -> {sort_list(make(vals))}")
