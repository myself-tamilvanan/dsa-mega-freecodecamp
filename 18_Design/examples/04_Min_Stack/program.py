"""LC 155 - Min Stack (two implementations)"""

class MinStackV1:
    """Parallel min-stack"""
    def __init__(self): self.stack=[]; self.min_stack=[]
    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
    def pop(self): self.stack.pop(); self.min_stack.pop()
    def top(self): return self.stack[-1]
    def getMin(self): return self.min_stack[-1]

class MinStackV2:
    """Single stack storing (val, min) tuples"""
    def __init__(self): self.stack=[]
    def push(self, val):
        cur_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, cur_min))
    def pop(self): self.stack.pop()
    def top(self): return self.stack[-1][0]
    def getMin(self): return self.stack[-1][1]

if __name__ == "__main__":
    for Cls in [MinStackV1, MinStackV2]:
        ms = Cls()
        for v in [5,-3,0,-3,2,-1]:
            ms.push(v)
        print(f"{Cls.__name__}:")
        print(f"  top={ms.top()}, min={ms.getMin()}")
        ms.pop()
        print(f"  After pop: top={ms.top()}, min={ms.getMin()}")
