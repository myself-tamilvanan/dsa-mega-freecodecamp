"""LC 217 - Contains Duplicate"""
def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen: return True
        seen.add(n)
    return False

if __name__=="__main__":
    cases = [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]
    for nums in cases:
        print(f"{nums} -> {contains_duplicate(nums)}")
