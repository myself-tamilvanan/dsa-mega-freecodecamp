"""LC 190 - Reverse Bits"""
def reverse_bits(n):
    result=0
    for _ in range(32):
        result=(result<<1)|(n&1)
        n>>=1
    return result
if __name__=="__main__":
    cases=[(43261596,964176192),(0,0),(4294967295,4294967295),(2147483648,1)]
    for n,expected in cases:
        result=reverse_bits(n)
        print(f"n={n:>12} bin={bin(n)[2:].zfill(32)[:16]}... -> {result} {'✓' if result==expected else '✗'}")
