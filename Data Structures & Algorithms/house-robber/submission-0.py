class Solution:
    def rob(self, nums: List[int]) -> int:
        p1, p2 = 0, 0

        for num in nums:
            temp = max(p1 + num, p2)
            p1 = p2
            p2 = temp

        return p2

        