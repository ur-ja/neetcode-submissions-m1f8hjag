class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = -1

        def dfs(row, col):
            if row not in range(ROWS) or col not in range(COLS) or grid[row][col] == 0 or (row, col) in visited:
                return 0
            visited.add((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area 


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col)
                    res = max(area, res)

        return res