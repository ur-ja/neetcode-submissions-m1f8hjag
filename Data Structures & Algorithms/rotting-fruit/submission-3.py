class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        minute = 0
        fresh = 0

        def addRotten(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visited or grid[r][c] != 1):
                return
            fresh -= 1
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addRotten(r, c + 1)
                addRotten(r + 1, c)
                addRotten(r, c - 1)
                addRotten(r - 1, c)
            minute += 1

        return minute if fresh == 0 else -1