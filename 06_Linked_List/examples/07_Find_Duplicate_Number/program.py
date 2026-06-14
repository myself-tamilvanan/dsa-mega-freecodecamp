"""LC 287 - Find the Duplicate Number"""
def find_duplicate(nums):
    # Floyd's cycle detection
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break
    # Find entry point of cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

if __name__ == "__main__":
    cases = [[1,3,4,2,2],[3,1,3,4,2],[1,1],[1,1,2]]
    for nums in cases:
        print(f"{nums} -> duplicate={find_duplicate(nums)}")
