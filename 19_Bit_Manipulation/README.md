# Chapter 19: Bit Manipulation
Work directly on binary for O(1) solutions.

## Key Operators
| Op | Symbol | Trick |
|----|--------|-------|
| AND | & | n & (n-1) clears lowest set bit |
| OR | \| | Set a bit: n \| (1<<k) |
| XOR | ^ | a^a=0, a^0=a (cancel pairs) |
| NOT | ~ | Flip all bits |
| Left shift | << | Multiply by 2 |
| Right shift | >> | Divide by 2 |

## LeetCode Problems
LC 136 Single Number, LC 191 Number of 1 Bits, LC 338 Counting Bits,
LC 190 Reverse Bits, LC 268 Missing Number, LC 371 Sum Without +
