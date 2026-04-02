class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]

        result = []
        for val in dictionary.values():
            result.append(val)

        return result
            
