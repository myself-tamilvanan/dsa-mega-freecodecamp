"""LC 155 - Min Stack"""
class MinStack:
    def __init__(self): self.s=[];self.ms=[]
    def push(self,v):
        self.s.append(v)
        self.ms.append(min(v, self.ms[-1] if self.ms else v))
    def pop(self): self.s.pop();self.ms.pop()
    def top(self): return self.s[-1]
    def get_min(self): return self.ms[-1]
if __name__=="__main__":
    ms=MinStack()
    for v in [3,-2,0]: ms.push(v)
    print("Top:", ms.top(), "Min:", ms.get_min())
    ms.pop()
    print("After pop - Min:", ms.get_min())
