"""Chapter 06: Linked List"""
import heapq

class ListNode:
    def __init__(self,val=0,next=None): self.val=val;self.next=next
    def __repr__(self):
        v=[];c=self
        while c: v.append(str(c.val));c=c.next
        return '->'.join(v)

def make(vals):
    d=ListNode(0);c=d
    for v in vals: c.next=ListNode(v);c=c.next
    return d.next

def reverse_list(head):
    p,c=None,head
    while c: n=c.next;c.next=p;p=c;c=n
    return p

def middle_node(head):
    s=f=head
    while f and f.next: s=s.next;f=f.next.next
    return s

def has_cycle(head):
    s=f=head
    while f and f.next:
        s=s.next;f=f.next.next
        if s==f: return True
    return False

def merge_two_lists(l1,l2):
    d=ListNode(0);c=d
    while l1 and l2:
        if l1.val<=l2.val: c.next=l1;l1=l1.next
        else: c.next=l2;l2=l2.next
        c=c.next
    c.next=l1 or l2
    return d.next

def remove_nth_from_end(head,n):
    d=ListNode(0,head);f=s=d
    for _ in range(n+1): f=f.next
    while f: s=s.next;f=f.next
    s.next=s.next.next
    return d.next

def reorder_list(head):
    s=f=head
    while f and f.next: s=s.next;f=f.next.next
    prev=None;sec=s.next;s.next=None
    while sec: tmp=sec.next;sec.next=prev;prev=sec;sec=tmp
    first=head;sec=prev
    while sec:
        t1,t2=first.next,sec.next
        first.next=sec;sec.next=t1
        first=t1;sec=t2
    return head

if __name__=="__main__":
    print("Reverse:", reverse_list(make([1,2,3,4,5])))
    print("Middle:", middle_node(make([1,2,3,4,5])))
    print("Has Cycle (no cycle):", has_cycle(make([1,2,3])))
    print("Merge Two:", merge_two_lists(make([1,2,4]),make([1,3,4])))
    print("Remove 2nd from end:", remove_nth_from_end(make([1,2,3,4,5]),2))
