class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of the frequency of each 
        # smh check in the dictionary the order of freqency and return top k?
        
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        pairs = []
        for key, value in freq.items():
            pairs.append((key, value))

        result = []
        for key, val in sorted(pairs, key=lambda x: x[1], reverse=True)[:k]:
            result.append(key)

        return result


        # should i put the values in a stack ? (but then they wouldnt neccessarily be in order)