class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()

        def dfs(c):
            if adj[c] == []:
                return True
            if c in visited:
                return False
            visited.add(c)
            for prereq in adj[c]:
                if not dfs(prereq):
                    return False
            adj[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True