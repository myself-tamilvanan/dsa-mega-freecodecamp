"""Chapter 07: Stack"""
from collections import defaultdict

def is_valid(s):
    st=[];pairs={')':'(','}':'{',']':'['}
    for c in s:
        if c in pairs:
            if not st or st[-1]!=pairs[c]: return False
            st.pop()
        else: st.append(c)
    return not st

class MinStack:
    def __init__(self): self.s=[];self.ms=[]
    def push(self,v): self.s.append(v);self.ms.append(min(v,self.ms[-1] if self.ms else v))
    def pop(self): self.s.pop();self.ms.pop()
    def top(self): return self.s[-1]
    def get_min(self): return self.ms[-1]

def daily_temperatures(T):
    res=[0]*len(T);st=[]
    for i,t in enumerate(T):
        while st and T[st[-1]]<t: j=st.pop();res[j]=i-j
        st.append(i)
    return res

def eval_rpn(tokens):
    st=[]
    for t in tokens:
        if t in '+-*/':
            b,a=st.pop(),st.pop()
            if t=='+': st.append(a+b)
            elif t=='-': st.append(a-b)
            elif t=='*': st.append(a*b)
            else: st.append(int(a/b))
        else: st.append(int(t))
    return st[0]

def largest_rectangle_area(heights):
    st=[];mx=0
    for i,h in enumerate(heights):
        start=i
        while st and st[-1][1]>h:
            idx,ht=st.pop();mx=max(mx,ht*(i-idx));start=idx
        st.append((start,h))
    for idx,ht in st: mx=max(mx,ht*(len(heights)-idx))
    return mx

if __name__=="__main__":
    print("Valid Parens '()[]{}':", is_valid("()[]{}"))
    ms=MinStack();[ms.push(v) for v in [3,1,2]]
    print("Min Stack min:", ms.get_min())
    print("Daily Temps:", daily_temperatures([73,74,75,71,69,72,76,73]))
    print("RPN ['2','1','+','3','*']:", eval_rpn(["2","1","+","3","*"]))
    print("Largest Rectangle [2,1,5,6,2,3]:", largest_rectangle_area([2,1,5,6,2,3]))
