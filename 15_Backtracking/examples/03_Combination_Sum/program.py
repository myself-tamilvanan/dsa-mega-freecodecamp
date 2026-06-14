"""LC 39 & 40 - Combination Sum I and II"""
def combination_sum(candidates, target):
    """Unlimited reuse"""
    result = []
    def backtrack(start, path, remaining):
        if remaining == 0: result.append(path[:]); return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining: break
            path.append(candidates[i])
            backtrack(i, path, remaining-candidates[i])  # i not i+1
            path.pop()
    candidates.sort()
    backtrack(0, [], target)
    return result

def combination_sum2(candidates, target):
    """LC 40 - Each number used once, no duplicate combinations"""
    result = []; candidates.sort()
    def backtrack(start, path, remaining):
        if remaining == 0: result.append(path[:]); return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining: break
            if i > start and candidates[i] == candidates[i-1]: continue  # skip dups
            path.append(candidates[i])
            backtrack(i+1, path, remaining-candidates[i])
            path.pop()
    backtrack(0, [], target)
    return result

if __name__ == "__main__":
    print("Combination Sum [2,3,6,7], target=7:", combination_sum([2,3,6,7],7))
    print("Combination Sum II [10,1,2,7,6,1,5], target=8:", combination_sum2([10,1,2,7,6,1,5],8))
