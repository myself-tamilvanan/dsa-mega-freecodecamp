"""LC 46 - Permutations"""
def permute(nums):
    result = []
    used = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:]); return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
    backtrack([])
    return result

def permute_unique(nums):
    """LC 47 - Permutations with duplicates"""
    result = []; nums.sort()
    used = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums): result.append(path[:]); return
        for i in range(len(nums)):
            if used[i]: continue
            if i > 0 and nums[i]==nums[i-1] and not used[i-1]: continue
            used[i]=True; path.append(nums[i]); backtrack(path)
            path.pop(); used[i]=False
    backtrack([]); return result

if __name__ == "__main__":
    print("Permutations [1,2,3]:")
    perms = permute([1,2,3])
    for p in perms: print(f"  {p}")
    print(f"Total: {len(perms)}")
    print("\nPermutations with dups [1,1,2]:")
    print(permute_unique([1,1,2]))
