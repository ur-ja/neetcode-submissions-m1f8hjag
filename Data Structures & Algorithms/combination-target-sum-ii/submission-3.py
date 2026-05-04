class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, path, total):
            if i == len(candidates) or total >= target:
                if total == target:
                    res.append(path.copy())
                return

            path.append(candidates[i])
            dfs(i + 1, path, total + candidates[i])

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1

            path.pop()
            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return res