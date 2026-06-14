class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)  # dummy
        self.tail = Node(0)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self._add_between(val, self.head, self.head.next)

    def addAtTail(self, val: int) -> None:
        self._add_between(val, self.tail.prev, self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        if index < 0: index = 0
        cur = self.head
        for _ in range(index):
            cur = cur.next
        self._add_between(val, cur, cur.next)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.size -= 1

    def _add_between(self, val, before, after):
        node = Node(val)
        node.prev = before
        node.next = after
        before.next = node
        after.prev = node
        self.size += 1

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    print(ll.get(1))  # 2
    ll.deleteAtIndex(1)
    print(ll.get(1))  # 3
