"""LC 128 - Longest Consecutive Sequence"""

def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for n in s:
        if n-1 not in s:  # start of sequence
            cur, streak = n, 1
            while cur+1 in s:
                cur+=1; streak+=1
            best = max(best, streak)
    return best

if __name__=="__main__":
    cases = [
        [100,4,200,1,3,2],
        [0,3,7,2,5,8,4,6,0,1],
        [],
        [1],
    ]
    for nums in cases:
        print(f"{nums} -> {longest_consecutive(nums)}")
