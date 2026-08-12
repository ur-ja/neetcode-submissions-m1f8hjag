class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def f(houses):
            r1, r2 = 0, 0
            for house in houses:
                temp = max(house + r2, r1)
                r2 = r1
                r1 = temp
            return r1

        return max(f(nums[:-1]), f(nums[1:]), nums[0])