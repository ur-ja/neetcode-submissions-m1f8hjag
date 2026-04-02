class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        GIVEN: nums[], k
        RETURN: k most frequest elements

        #1
        dictionary that stores the frequency of elements and then
        returns based on k - did not understand it right

        #2 
        sort dict based on vals - not optimal

        #3 #4 - heap and bucket sort

        """

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]

        for key, val in count.items():
            freq[val].append(key)


        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if len(result) < k:
                    result.append(num)

        return result