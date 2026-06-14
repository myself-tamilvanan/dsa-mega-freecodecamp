"""LC 138 - Copy List with Random Pointer"""
class Node:
    def __init__(self,v,next=None,random=None): self.val=v;self.next=next;self.random=random

def copy_random_list(head):
    if not head: return None
    # Step 1: Interleave clones
    curr = head
    while curr:
        clone = Node(curr.val, curr.next)
        curr.next = clone
        curr = clone.next
    # Step 2: Set random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    # Step 3: Separate lists
    old_head = head; new_head = head.next
    curr_old = old_head; curr_new = new_head
    while curr_old:
        curr_old.next = curr_old.next.next
        curr_new.next = curr_new.next.next if curr_new.next else None
        curr_old = curr_old.next
        curr_new = curr_new.next
    return new_head

if __name__ == "__main__":
    # Build: [7,null]->[13,0]->[11,4]->[10,2]->[1,0]
    nodes = [Node(i) for i in [7,13,11,10,1]]
    nodes[0].next=nodes[1];nodes[1].next=nodes[2];nodes[2].next=nodes[3];nodes[3].next=nodes[4]
    nodes[1].random=nodes[0];nodes[2].random=nodes[4];nodes[3].random=nodes[2];nodes[4].random=nodes[0]
    cloned = copy_random_list(nodes[0])
    vals=[]
    c=cloned
    while c: vals.append((c.val, c.random.val if c.random else None));c=c.next
    print("Cloned list (val, random_val):", vals)
    print("Is new object:", cloned is not nodes[0])
