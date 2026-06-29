class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs 
        # num of bfs till all in visited 
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        fresh = 0
        minute = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    visited.add((row, col))
                    q.append((row, col))

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or 
                        (nr, nc) in visited or grid[nr][nc] != 1):
                        continue
                    fresh -= 1
                    visited.add((nr, nc))
                    q.append([nr, nc])

            minute += 1

        return minute if fresh == 0 else -1
