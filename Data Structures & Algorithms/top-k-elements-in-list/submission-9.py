class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TOP K = HEAP or BUCKET SORT
        # count = index, num = val

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # since count can range from 0 to the total numbers in the 
        # array at max
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for c in range(len(freq) - 1, -1, -1):
            for n in freq[c]:
                res.append(n)
            if len(res) == k:
                return res
        return res