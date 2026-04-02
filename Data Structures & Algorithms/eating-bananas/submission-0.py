class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = r

        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            if total_time <= h:
                r = k - 1
                minK = min(k, minK)
            else:
                l = k + 1

        return minK