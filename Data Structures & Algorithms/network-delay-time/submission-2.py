class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}

        for src, dst, cost in times:
            adj[src].append((dst, cost))

        minHeap = [(0, k)] # (cost, src)
        visited = set()
        t = 0

        while minHeap:
            c1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, c1) # time gets incremented to the lowest time in the heap we have spent
            for n2, c2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [c1 + c2, n2])

        return t if len(visited) == n else -1 

