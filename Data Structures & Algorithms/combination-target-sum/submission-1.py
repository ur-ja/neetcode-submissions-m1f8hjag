class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, curSum):
            if curSum == target:
                res.append(path.copy())
                return
            if curSum > target or i >= len(nums):
                return

            path.append(nums[i])
            curSum += nums[i]
            if i < len(nums) and curSum < target:
                dfs(i, path, curSum)
            else:
                dfs(i + 1, path, curSum)

            path.pop()
            curSum -= nums[i]
            dfs(i + 1, path, curSum)

        dfs(0, [], 0)

        return res