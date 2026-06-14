"""LC 268 - Missing Number"""
def missing_number_xor(nums):
    result = len(nums)
    for i, n in enumerate(nums):
        result ^= i ^ n
    return result

def missing_number_math(nums):
    n = len(nums)
    return n*(n+1)//2 - sum(nums)

if __name__ == "__main__":
    cases = [[3,0,1],[0,1],[9,6,4,2,3,5,7,0,1],[0]]
    for nums in cases:
        xor  = missing_number_xor(nums)
        math = missing_number_math(nums)
        print(f"{nums} -> XOR={xor}, Math={math}, Match={xor==math}")
