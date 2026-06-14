"""LC 622 - Design Circular Queue"""
class MyCircularQueue:
    def __init__(self,k): self.q=[0]*k;self.head=0;self.cnt=0;self.sz=k
    def enQueue(self,val):
        if self.isFull(): return False
        self.q[(self.head+self.cnt)%self.sz]=val;self.cnt+=1;return True
    def deQueue(self):
        if self.isEmpty(): return False
        self.head=(self.head+1)%self.sz;self.cnt-=1;return True
    def Front(self): return -1 if self.isEmpty() else self.q[self.head]
    def Rear(self): return -1 if self.isEmpty() else self.q[(self.head+self.cnt-1)%self.sz]
    def isEmpty(self): return self.cnt==0
    def isFull(self): return self.cnt==self.sz
if __name__=="__main__":
    cq=MyCircularQueue(3)
    print(cq.enQueue(1),cq.enQueue(2),cq.enQueue(3))
    print("Front:",cq.Front(),"Rear:",cq.Rear(),"Full:",cq.isFull())
    cq.deQueue()
    print("After deQueue - Front:",cq.Front())
