class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)

        visited = set()
        res = []

        def dfs(c):
            if c in visited:
                return False
            if adj[c] == []:
                res.append(c)
                return True

            visited.add(c)

            for p in adj[c]:
                if not dfs(p):
                    return False
            res.append(c)
            visited.remove(c)
            adj[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res