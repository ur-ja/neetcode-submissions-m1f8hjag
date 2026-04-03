class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            d = -(x**2 + y**2)
            heapq.heappush(maxHeap, [d, [x, y]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []

        for d, point in maxHeap:
            res.append(point)

        return res