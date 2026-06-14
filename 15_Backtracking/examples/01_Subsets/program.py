"""LC 78 - Subsets"""
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return result

def subsets_iterative(nums):
    """Build up: for each num, add it to all existing subsets"""
    result = [[]]
    for n in nums:
        result += [sub + [n] for sub in result]
    return result

if __name__ == "__main__":
    nums = [1,2,3]
    bt = subsets(nums)
    it = subsets_iterative(nums)
    print(f"Backtracking ({len(bt)} subsets): {sorted(bt)}")
    print(f"Iterative   ({len(it)} subsets): {sorted(it)}")
    print(f"Equal: {sorted(bt)==sorted(it)}")
