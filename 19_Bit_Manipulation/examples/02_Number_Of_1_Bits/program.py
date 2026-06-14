"""LC 191 - Number of 1 Bits (Hamming Weight)"""
def hamming_weight(n):
    """Brian Kernighan's algorithm - only loops for each set bit"""
    count = 0
    while n:
        n &= n - 1  # clear lowest set bit
        count += 1
    return count

def hamming_weight_v2(n):
    """Check each bit"""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def hamming_distance(x, y):
    """LC 461 - XOR then count set bits"""
    return hamming_weight(x ^ y)

if __name__ == "__main__":
    nums = [0, 1, 11, 128, 0xFFFFFFFF, 43261596]
    for n in nums:
        hw = hamming_weight(n)
        print(f"n={n:>12} (bin: {bin(n)}) -> {hw} set bits")
    print("\nHamming Distance:")
    for x,y in [(1,4),(93,73)]:
        print(f"  hamming_distance({x},{y}) = {hamming_distance(x,y)}")
