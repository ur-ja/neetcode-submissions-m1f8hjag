class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def f(i):
            if i >= n:
                return 0
                
            # pick 
            left = nums[i] + f(i + 2)

            # not pick
            right = f(i + 1)

            return max(left, right)

        return f(0)
            
        