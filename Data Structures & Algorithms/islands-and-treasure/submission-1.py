class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or (nr, nc) in visited or
                        nr == ROWS or nc == COLS or grid[nr][nc] == -1):
                        continue
                    visited.add((nr, nc))
                    q.append([nr, nc])

            dist += 1