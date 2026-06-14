from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def list_to_arr(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    sol = Solution()
    print(list_to_arr(sol.middleNode(make_list([1,2,3,4,5]))))    # [3,4,5]
    print(list_to_arr(sol.middleNode(make_list([1,2,3,4,5,6]))))  # [4,5,6]
    print(list_to_arr(sol.middleNode(make_list([1]))))             # [1]
