"""LC 42 - Trapping Rain Water"""
def trap(height):
    l, r = 0, len(height)-1
    lm = rm = water = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= lm: lm = height[l]
            else: water += lm - height[l]
            l += 1
        else:
            if height[r] >= rm: rm = height[r]
            else: water += rm - height[r]
            r -= 1
    return water

if __name__=="__main__":
    cases=[[0,1,0,2,1,0,1,3,2,1,2,1],[4,2,0,3,2,5]]
    for h in cases:
        print(f"{h} -> {trap(h)}")
