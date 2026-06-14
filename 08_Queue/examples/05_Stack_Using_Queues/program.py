"""LC 225 - Implement Stack Using Queues"""
from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # main queue
        self.q2 = deque()  # temp queue

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

if __name__ == "__main__":
    stack = MyStack()
    for v in [1, 2, 3]: stack.push(v)
    print("top:", stack.top())     # 3
    print("pop:", stack.pop())     # 3
    print("top:", stack.top())     # 2
    print("empty:", stack.empty()) # False
    stack.pop(); stack.pop()
    print("empty:", stack.empty()) # True
