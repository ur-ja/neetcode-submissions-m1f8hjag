class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()

        def addRotten(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visited or grid[r][c] == 0):
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append([r, c])

        minute = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addRotten(r, c + 1)
                addRotten(r + 1, c)
                addRotten(r, c - 1)
                addRotten(r - 1, c)
            minute += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minute