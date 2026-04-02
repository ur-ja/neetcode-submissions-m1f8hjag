class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob2(houses: List[int]):
            h1, h2 = 0, 0

            for house in houses:
                temp = max(h1 + house, h2)
                h1 = h2
                h2 = temp

            return h2

        return max(nums[0], rob2(nums[1:]), rob2(nums[:len(nums) - 1]))

