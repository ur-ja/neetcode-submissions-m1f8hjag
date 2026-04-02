class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # number = index, count = value 
        # but number can be anything so this doesnt work

        # modified bucket sort
        # count = index, number/s = value

        # another way to do it is with min heap since it gives
        # the highest val so make dictionary and convert it to heap
        # then pop out top k times 

        # so for top k heap and bucket sort

        count = {} # length n so space O(n)

        # runs n times
        for n in nums:
            count[n] = 1 + count.get(n, 0) # O(1)

        # O(n)
        freq = [[] for i in range(len(nums) + 1)]

        # O(n)
        for n, c in count.items():
            freq[c].append(n) # O(1)

        result = [] # space max n beacuse max number of times a number can occur = length of array

        # O(n)
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result


        # O(n) = time
        # O(n) = space

        return []