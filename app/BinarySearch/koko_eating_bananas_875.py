"""
875. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`.
Each hour, she chooses some pile of bananas and eats `k` bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within h hours.


Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""
from typing import List


class Solution:
    """
    Think of it as finding the slowest eating speed that still finishes all bananas before the deadline.
    We try a speed: if it’s too slow and misses the time, we increase it; if it finishes on time, we try a bit slower.
    Since “faster speed means less time” is consistent, we can narrow the range efficiently to find the minimum speed
    that works.
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # because k is in [1, max(piles)], we can use binary search to find the minimum k
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            ok = self.can_finish(piles, h, mid)
            print(f"\nleft={left}, right={right}, mid = {mid}, ok={ok}")
            if ok:
                right = mid
            else:
                left = mid + 1

        print(f"\nreturn {left}")
        return left

    def can_finish(self, piles: List[int], h: int, k: int) -> bool:
        total = 0

        # Calculate the total hours needed to eat all bananas at speed k
        for p in piles:
            total += (p + k - 1) // k # # same as ceil(p / k)

        return total <= h

