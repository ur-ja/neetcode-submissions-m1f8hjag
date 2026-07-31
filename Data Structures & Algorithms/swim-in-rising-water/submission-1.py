class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            tmax, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return tmax
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and nr >= 0 and nc >= 0 and nr < N and nc < N:
                    nt = max(tmax, grid[nr][nc])
                    heapq.heappush(minHeap, [nt , nr, nc])

        return -1
