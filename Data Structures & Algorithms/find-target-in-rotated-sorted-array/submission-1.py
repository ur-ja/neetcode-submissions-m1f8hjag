class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                # we are in the left sorted portion
                if target > nums[m] or target < nums[l]:
                    # if target is greter than the largest number in left go right
                    # or
                    # if target is smaller than the smallest number in left go right
                    l = m + 1
                else:
                    r = m - 1
            else:
                # we are in the right sorted portion
                if target < nums[m] or target > nums[r]:
                    # if target is greater than the largest number in right go left
                    # or
                    # if target is smaller than the smallest number in right go left 
                    r = m - 1
                else:
                    l = m + 1

        return -1

            
                
        