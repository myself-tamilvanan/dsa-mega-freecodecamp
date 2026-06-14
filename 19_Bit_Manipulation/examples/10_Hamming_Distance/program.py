class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingDistance(1, 4))  # 2
    print(sol.hammingDistance(3, 1))  # 1
    print(sol.hammingDistance(0, 0))  # 0
