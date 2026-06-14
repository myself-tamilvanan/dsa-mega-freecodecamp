"""LC 55 & 45 - Jump Game I and II"""
def can_jump(nums):
    """Can we reach the end?"""
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach: return False
        max_reach = max(max_reach, i + jump)
    return True

def min_jumps(nums):
    """LC 45 - Minimum jumps to reach end"""
    jumps = cur_end = farthest = 0
    for i in range(len(nums)-1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps

if __name__ == "__main__":
    cases = [[2,3,1,1,4],[3,2,1,0,4],[0],[1,1,1,1]]
    for nums in cases:
        print(f"{nums} -> can_jump={can_jump(nums)}, min_jumps={min_jumps(nums)}")
