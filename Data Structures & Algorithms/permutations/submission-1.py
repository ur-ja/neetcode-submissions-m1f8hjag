class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        # get permutations of rest of the array
        permutations = self.permute(nums[1:])
        res = []

        # we need to insert the current number
        # one by one at each position of each of the permutations
        # this is because order matters in permutation 
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                permutation_copy = permutation.copy()
                permutation_copy.insert(i, nums[0])
                res.append(permutation_copy)

        return res
            
            