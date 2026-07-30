class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = { i : [] for i in range(n)}

        for i in range(n):
            x, y = points[i]
            for j in range(i + 1, n):
                a, b = points[j]
                dist = abs(x - a) + abs(y - b)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
                
        minHeap = [[0, 0]]
        visited = set()
        res = 0

        while minHeap:
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += dist
            for cost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [cost, nei])

        return res
                    