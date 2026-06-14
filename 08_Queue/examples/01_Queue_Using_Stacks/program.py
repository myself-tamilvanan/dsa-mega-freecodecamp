"""LC 232 - Queue Using Stacks"""
class MyQueue:
    def __init__(self): self.inp=[];self.out=[]
    def push(self,x): self.inp.append(x)
    def _move(self):
        if not self.out:
            while self.inp: self.out.append(self.inp.pop())
    def pop(self): self._move();return self.out.pop()
    def peek(self): self._move();return self.out[-1]
    def empty(self): return not self.inp and not self.out
if __name__=="__main__":
    q=MyQueue()
    q.push(1);q.push(2);q.push(3)
    print("peek:", q.peek())
    print("pop:", q.pop())
    print("pop:", q.pop())
    print("empty:", q.empty())
