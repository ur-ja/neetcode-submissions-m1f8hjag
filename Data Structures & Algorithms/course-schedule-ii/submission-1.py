class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return False 
            if preMap[crs] == []:
                res.append(crs)
                return True
            if preMap[crs] == [-1]:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            res.append(crs)
            visited.remove(crs)
            preMap[crs] = [-1]
            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res