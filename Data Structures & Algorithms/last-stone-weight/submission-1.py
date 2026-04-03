from _heapq import heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            if x < y:
                y = y - x
                heappush(stones, -y)
            else:
                x = x - y
                heappush(stones, -x)

        return -stones[0]