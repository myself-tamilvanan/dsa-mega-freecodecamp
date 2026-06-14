"""LC 167 - Two Sum II"""
def two_sum_ii(numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l]+numbers[r]
        if s == target: return [l+1, r+1]
        elif s < target: l+=1
        else: r-=1
    return []

if __name__=="__main__":
    cases = [([2,7,11,15],9),([2,3,4],6),([-1,0],[-1+0])]
    for nums,t in cases:
        print(f"{nums}, target={t} -> {two_sum_ii(nums,t)}")
