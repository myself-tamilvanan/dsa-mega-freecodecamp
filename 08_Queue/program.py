"""Chapter 08: Queue"""
from collections import deque

class MyQueue:
    def __init__(self): self.inp=[];self.out=[]
    def push(self,x): self.inp.append(x)
    def _move(self):
        if not self.out:
            while self.inp: self.out.append(self.inp.pop())
    def pop(self): self._move();return self.out.pop()
    def peek(self): self._move();return self.out[-1]
    def empty(self): return not self.inp and not self.out

def open_lock(deadends, target):
    dead=set(deadends)
    if "0000" in dead: return -1
    if target=="0000": return 0
    q=deque([("0000",0)]);vis={"0000"}
    while q:
        state,turns=q.popleft()
        for i in range(4):
            for d in [1,-1]:
                nd=str((int(state[i])+d)%10)
                ns=state[:i]+nd+state[i+1:]
                if ns==target: return turns+1
                if ns not in vis and ns not in dead:
                    vis.add(ns);q.append((ns,turns+1))
    return -1

def predict_party_victory(senate):
    R,D=deque(),deque();n=len(senate)
    for i,s in enumerate(senate):
        (R if s=='R' else D).append(i)
    while R and D:
        r,d=R.popleft(),D.popleft()
        if r<d: R.append(r+n)
        else: D.append(d+n)
    return "Radiant" if R else "Dire"

if __name__=="__main__":
    q=MyQueue();q.push(1);q.push(2);q.push(3)
    print("Queue pop:", q.pop(), "peek:", q.peek())
    print("Open Lock:", open_lock(["0201","0101","0102","1212","2002"],"0202"))
    print("DOTA2 Senate 'RDD':", predict_party_victory("RDD"))
