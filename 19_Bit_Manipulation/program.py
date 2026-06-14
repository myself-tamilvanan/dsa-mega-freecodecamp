"""Chapter 19: Bit Manipulation"""

def single_number(nums):
    res=0
    for n in nums: res^=n
    return res

def hamming_weight(n):
    cnt=0
    while n: n&=n-1;cnt+=1
    return cnt

def count_bits(n):
    dp=[0]*(n+1)
    for i in range(1,n+1): dp[i]=dp[i>>1]+(i&1)
    return dp

def missing_number(nums):
    res=len(nums)
    for i,n in enumerate(nums): res^=i^n
    return res

def reverse_bits(n):
    res=0
    for _ in range(32): res=(res<<1)|(n&1);n>>=1
    return res

def get_sum(a,b):
    mask=0xFFFFFFFF
    while b&mask: a,b=a^b,(a&b)<<1
    return (a&mask) if b>0 else a

if __name__=="__main__":
    print("Single Number [4,1,2,1,2]:", single_number([4,1,2,1,2]))
    print("Hamming Weight(11):", hamming_weight(11))
    print("Count Bits(5):", count_bits(5))
    print("Missing Number [3,0,1]:", missing_number([3,0,1]))
    print("Sum 1+2:", get_sum(1,2))
