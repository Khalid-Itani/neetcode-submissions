import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / m)
            if hours <= h:          # m works
                ans = m
                r = m - 1           # try smaller k
            else:                   # m too slow
                l = m + 1
        return ans

            