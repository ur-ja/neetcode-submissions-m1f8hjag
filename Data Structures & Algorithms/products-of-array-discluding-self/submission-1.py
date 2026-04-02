class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1 for i in range(len(nums))]
        result = []

        p = 1
        prefix.append(p)
        for i in range(1, len(nums)):
            p *= nums[i - 1]
            prefix.append(p)

        s = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                s = 1
            else:
                s *= nums[i + 1]
            suffix[i] = s

        for i, num in enumerate(nums):
            result.append(prefix[i] * suffix[i])

        return result

