class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)

        processed = set()
        cycle = set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            if c in processed:
                return True

            cycle.add(c)

            for p in adj[c]:
                if not dfs(p):
                    return False
            res.append(c)
            cycle.remove(c)
            processed.add(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res