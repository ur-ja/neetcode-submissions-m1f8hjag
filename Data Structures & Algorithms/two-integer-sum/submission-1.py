class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            num_required = target - num
            if num_required in indices:
                return [indices[num_required], i]
            else:
                indices[num] = i

        return [-1, -1]