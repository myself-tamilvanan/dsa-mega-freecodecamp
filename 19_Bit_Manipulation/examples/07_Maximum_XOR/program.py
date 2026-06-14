"""LC 421 - Maximum XOR of Two Numbers in an Array"""
def find_maximum_xor(nums):
    max_xor=0;mask=0
    for i in range(31,-1,-1):
        mask|=(1<<i)
        prefixes={n&mask for n in nums}
        candidate=max_xor|(1<<i)
        if any(candidate^p in prefixes for p in prefixes):
            max_xor=candidate
    return max_xor
if __name__=="__main__":
    cases=[([3,10,5,25,2,8],28),([14,70,53,83,49,91,36,80,92,51,66,70],127),([0],0)]
    for nums,expected in cases:
        result=find_maximum_xor(nums)
        print(f"{nums} -> {result} {'✓' if result==expected else '✗'}")
