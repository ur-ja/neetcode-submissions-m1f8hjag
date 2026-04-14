class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, total):
            if i >= len(nums):
                if total == target:
                    res.append(path)
                return True
            
            path.append(nums[i])
            dfs(i + 1, path, total + nums[i])

            path.pop()