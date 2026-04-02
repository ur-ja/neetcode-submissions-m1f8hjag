class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        GIVEN: nums[], k
        RETURN: k most frequest elements

        #1
        dictionary that stores the frequency of elements and then
        returns based on k

        """

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # for w in sorted(d, key=d.get, reverse=True):
        #print(w, d[w])
        values = sorted(count.values(), reverse=True)[0:k]

        result = []
        for key, val in count.items():
            if val in values:
                result.append(key)


        return result