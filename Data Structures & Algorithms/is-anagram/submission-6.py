class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = self.getDict(s)
        t_dict = self.getDict(t)

        # O(k)
        return s_dict == t_dict

    def getDict(self, word: str) -> dict:
        freq = {}

        # O(n)
        for letter in word:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        
        return freq