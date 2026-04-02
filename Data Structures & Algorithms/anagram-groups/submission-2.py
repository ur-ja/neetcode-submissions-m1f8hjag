class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # space = O(n)

        #O(n)
        for word in strs:
            key = str(sorted(word)) # O(klogk)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        result = []
        # O(n)
        for key, value in anagrams.items():
            result.append(value)

        # total complexity = O(nklogn)

        return result