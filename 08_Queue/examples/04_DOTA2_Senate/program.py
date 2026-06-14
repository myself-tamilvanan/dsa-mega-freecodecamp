"""LC 649 - DOTA2 Senate"""
from collections import deque
def predict_party_victory(senate):
    R,D=deque(),deque();n=len(senate)
    for i,s in enumerate(senate):
        (R if s=='R' else D).append(i)
    while R and D:
        r,d=R.popleft(),D.popleft()
        (R if r<d else D).append((r if r<d else d)+n)
    return "Radiant" if R else "Dire"
if __name__=="__main__":
    cases=["RD","RDD","DDRRR","DRRD"]
    for s in cases:
        print(f"'{s}' -> {predict_party_victory(s)}")
