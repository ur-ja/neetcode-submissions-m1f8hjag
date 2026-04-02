class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurances = {}

        for num in nums:
            if num in occurances:
                return True
            else:
                occurances[num] = 1
                
        return False
