class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            maxH, row, col = heapq.heappop(minHeap)
            if row == N - 1 and col == N - 1:
                return maxH
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if ((r, c) not in visited and r < N and c < N and r >= 0 and c >= 0):
                    newMaxH = max(maxH, grid[r][c])
                    heapq.heappush(minHeap, (newMaxH, r, c))

        return -1