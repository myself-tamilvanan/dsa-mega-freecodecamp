from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]
                for i in range(groupSize):
                    if count[card + i] < freq:
                        return False
                    count[card + i] -= freq
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # True
    print(sol.isNStraightHand([1,2,3,4,5], 4))           # False
    print(sol.isNStraightHand([1,2,3], 3))                # True
