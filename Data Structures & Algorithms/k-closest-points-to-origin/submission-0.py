class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for point in points:
            x, y = point[0], point[1]
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(distances, [d, point])

        res = []
        while len(distances) > 0 and k > 0:
            [d, point] = heapq.heappop(distances)
            res.append(point)
            k -= 1

        return res
