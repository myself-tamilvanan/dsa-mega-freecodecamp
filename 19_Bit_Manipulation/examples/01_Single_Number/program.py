"""LC 136 & 137 - Single Number I and II"""
def single_number(nums):
    """Every element twice except one. XOR all."""
    result = 0
    for n in nums: result ^= n
    return result

def single_number_ii(nums):
    """LC 137 - Every element appears 3 times except one.
    Use bit counting: for each bit, count % 3 gives lone number's bit."""
    result = 0
    for i in range(32):
        bit_sum = sum((n >> i) & 1 for n in nums) % 3
        result |= bit_sum << i
    # Handle negative numbers in Python
    if result >= 2**31: result -= 2**32
    return result

if __name__ == "__main__":
    cases1 = [[4,1,2,1,2],[2,2,1],[1]]
    for nums in cases1:
        print(f"Single Number I {nums} -> {single_number(nums)}")
    cases2 = [[2,2,3,2],[0,1,0,1,0,1,99]]
    for nums in cases2:
        print(f"Single Number II {nums} -> {single_number_ii(nums)}")
