"""LC 84 - Largest Rectangle in Histogram"""
def largest_rectangle_area(heights):
    stack = []  # (start_index, height)
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, ht = stack.pop()
            max_area = max(max_area, ht*(i-idx))
            start = idx
        stack.append((start, h))
    for idx, ht in stack:
        max_area = max(max_area, ht*(len(heights)-idx))
    return max_area
if __name__=="__main__":
    cases=[[2,1,5,6,2,3],[2,4],[6,7,5,2,4,5,9,3],[1],[1,1]]
    for h in cases:
        print(f"{h} -> {largest_rectangle_area(h)}")
