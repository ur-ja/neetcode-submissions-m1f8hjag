class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        maxLength = 0
        for num in nums:
            if num - 1 not in count:
                length = 0
                while num + length in count:
                    length += 1
                maxLength = max(length, maxLength)

        return maxLength

        

        