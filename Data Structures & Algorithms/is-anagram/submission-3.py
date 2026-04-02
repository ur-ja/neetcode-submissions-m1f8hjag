class Solution:
    def getFrequency(self, word):
        freq = {}

        for letter in word:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1

        return freq
        
    def isAnagram(self, s: str, t: str) -> bool:

        s_freq = self.getFrequency(s)
        t_freq = self.getFrequency(t)

        return s_freq == t_freq

        
