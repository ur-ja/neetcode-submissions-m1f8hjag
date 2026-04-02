class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in numset:
                continue

            curr = num
            length = 0
            while curr in numset:
                length += 1
                curr += 1

            longest = max(longest, length)

        return longest     
                

        