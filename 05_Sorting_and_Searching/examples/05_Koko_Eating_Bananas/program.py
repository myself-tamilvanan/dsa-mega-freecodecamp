"""LC 875 - Koko Eating Bananas"""
import math

def min_eating_speed(piles, h):
    l, r = 1, max(piles)
    def can_finish(k):
        return sum(math.ceil(p/k) for p in piles) <= h
    while l < r:
        m = (l+r)//2
        if can_finish(m): r=m
        else: l=m+1
    return l

if __name__=="__main__":
    cases=[([3,6,7,11],8),([30,11,23,4,20],5),([312884470],312884469)]
    for piles,h in cases:
        print(f"piles={piles}, h={h} -> min speed={min_eating_speed(piles,h)}")
