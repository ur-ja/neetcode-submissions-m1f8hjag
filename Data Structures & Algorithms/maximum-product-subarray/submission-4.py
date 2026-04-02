class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maximum, minimum = 1, 1

        for num in nums:
            if num == 0:
                maximum, minimum = 1, 1
                continue  
            temp = maximum * num
            maximum = max(num * maximum, num * minimum, num)
            minimum = min(temp, num * minimum, num)
            res = max(maximum, res)
        return res