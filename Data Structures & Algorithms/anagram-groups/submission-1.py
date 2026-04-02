class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in freq:
                freq[key].append(word)
            else:
                freq[key] = [word]

        result = []
        for arr in freq.values():
            result.append(arr)

        return result
