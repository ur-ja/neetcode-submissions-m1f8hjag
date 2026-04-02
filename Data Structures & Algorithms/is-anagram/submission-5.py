class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.getDict(s)
        t_dict = self.getDict(t)

        return s_dict == t_dict

    def getDict(self, word: str) -> dict:
        freq = {}

        for letter in word:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        
        return freq