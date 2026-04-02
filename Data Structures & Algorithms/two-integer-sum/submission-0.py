class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

        given: nums[], target
        return: 2 indices i and j such that nums[i] + nums[j] == target and i != j

        you can assume that i and j exist


        """

        occurances = {}

        for i, num in enumerate(nums):
            required_num = target - num
            if required_num in occurances and i != occurances[required_num]:
                return [occurances[required_num],i]
            occurances[num] = i

        return [-1, -1]

        
        