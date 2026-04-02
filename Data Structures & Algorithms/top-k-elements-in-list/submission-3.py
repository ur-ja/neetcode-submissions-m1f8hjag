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

        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap) # popping removes the element with the smallest freq since this is min heap
        
        return [num for _, num in heap]