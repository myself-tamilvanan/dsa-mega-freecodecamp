"""LC 752 - Open the Lock"""
from collections import deque
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
if __name__=="__main__":
    cases=[(["0201","0101","0102","1212","2002"],"0202"),(["8888"],"0009"),(["8887","8889","8878","8898","8788","8988","7888","9888"],"8888")]
    for dead,t in cases:
        print(f"target='{t}' -> {open_lock(dead,t)} turns")
