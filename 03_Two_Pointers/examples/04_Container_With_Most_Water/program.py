"""LC 11 - Container With Most Water"""
def max_area(height):
    l, r = 0, len(height)-1
    result = 0
    while l < r:
        area = (r-l) * min(height[l], height[r])
        result = max(result, area)
        if height[l] < height[r]: l+=1
        else: r-=1
    return result

if __name__=="__main__":
    cases=[[1,8,6,2,5,4,8,3,7],[1,1],[4,3,2,1,4],[1,2,1]]
    for h in cases:
        print(f"{h} -> {max_area(h)}")
