"""LC 269 - Alien Dictionary"""
from collections import defaultdict, deque

def alien_order(words):
    adj=defaultdict(set)
    indegree={c:0 for w in words for c in w}
    for i in range(len(words)-1):
        w1,w2=words[i],words[i+1]
        min_len=min(len(w1),len(w2))
        if len(w1)>len(w2) and w1[:min_len]==w2[:min_len]: return ""
        for j in range(min_len):
            if w1[j]!=w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]]+=1
                break
    q=deque(c for c in indegree if indegree[c]==0)
    order=[]
    while q:
        c=q.popleft();order.append(c)
        for nb in adj[c]:
            indegree[nb]-=1
            if indegree[nb]==0: q.append(nb)
    return ''.join(order) if len(order)==len(indegree) else ""
if __name__=="__main__":
    cases=[["wrt","wrf","er","ett","rftt"],["z","x"],["z","x","z"]]
    for words in cases:
        print(f"{words} -> '{alien_order(words)}'")
