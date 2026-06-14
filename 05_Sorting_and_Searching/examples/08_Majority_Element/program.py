"""LC 169 - Majority Element"""
def majority_element(nums):
    candidate, count = None, 0
    for n in nums:
        if count == 0: candidate = n
        count += 1 if n == candidate else -1
    return candidate

def majority_element_sort(nums):
    """Sorting approach: middle element is always majority"""
    return sorted(nums)[len(nums)//2]

if __name__ == "__main__":
    cases = [[3,2,3],[2,2,1,1,1,2,2],[1]]
    for nums in cases:
        bm = majority_element(nums)
        srt = majority_element_sort(nums)
        print(f"{nums} -> Boyer-Moore={bm}, Sort={srt}")
