class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return 

            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                dfs(nei, node)

        res = 0
        for node in range(n):
            if node in visited:
                continue
            dfs(node, -1)
            res += 1

        return res
