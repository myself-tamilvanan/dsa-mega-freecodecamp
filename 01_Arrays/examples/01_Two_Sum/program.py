"""LC 1 - Two Sum"""
def two_sum(nums, target):
    seen = {}  # val -> index
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i
    return []

if __name__=="__main__":
    cases = [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([3,3], 6),
    ]
    for nums, target in cases:
        print(f"two_sum({nums}, {target}) = {two_sum(nums, target)}")
