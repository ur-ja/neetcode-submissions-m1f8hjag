class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(n)}

        for node, nei in edges:
            adjMap[node].append(nei)
            adjMap[nei].append(node)

        print(adjMap)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            if adjMap[node] == []:
                return True

            visited.add(node)
            for nei in adjMap[node]:
                if nei != prev:
                    if not dfs(nei, node): return False

            visited.remove(node)
            adjMap[node] = []
            return True

        for node in range(n):
            if not dfs(node, -1): return False

        return True
        