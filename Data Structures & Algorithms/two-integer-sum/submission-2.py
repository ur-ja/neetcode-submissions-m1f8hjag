class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [5,5,0,20] target = 25
        freq = {}
        for i, num in enumerate(nums):
            num_req = target - num
            if num_req in freq:
                return [freq[num_req], i]
            else:
                freq[num] = i

        return [-1, -1]