"""LC 179 - Largest Number"""
from functools import cmp_to_key

def largest_number(nums):
    def compare(a, b):
        return 1 if str(a)+str(b) < str(b)+str(a) else -1
    sorted_nums = sorted(nums, key=cmp_to_key(compare))
    result = ''.join(map(str, sorted_nums))
    return '0' if result[0] == '0' else result

if __name__ == "__main__":
    cases = [[10,2],[3,30,34,5,9],[0,0],[1],[999999998,999999997,999999999]]
    for nums in cases:
        print(f"{nums} -> '{largest_number(nums)}'")
