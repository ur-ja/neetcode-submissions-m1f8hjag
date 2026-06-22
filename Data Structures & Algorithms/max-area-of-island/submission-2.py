class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(row, col):
            if (row not in range(rows) or col not in range(cols) or
                (row, col) in visited or grid[row][col] == 0):
                return 0
            visited.add((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    maxArea = max(area, maxArea)

        return maxArea