class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(rc, cc):
            q = collections.deque()
            visited.add((rc, cc))
            q.append((rc, cc))

            while q:
                row, col = q.popleft()
                neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for neighbour in neighbours:
                    r, c = row + neighbour[0], col + neighbour[1]

                    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1" or (r, c) in visited:
                        continue
                    else:
                        visited.add((r,c))
                        q.append((r,c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    # we do a bfs to check off all surrounding 1's
                    bfs(row, col)
                    # we then update the number of islands
                    islands += 1


        return islands