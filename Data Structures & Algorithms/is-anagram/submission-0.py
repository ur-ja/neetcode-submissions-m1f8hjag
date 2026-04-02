class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given: string s and string t
        return: True if s and t are anagrams
                False otherwise

        anagram: exact same characters

        sets not poss because number of occurances will not be counted

        dictionary makes sense we can keep a tally of how many times each letter has occurred
        then compare
        """

        def getOccurances(word: str):
            occurances = {}
            for letter in word:
                if letter in occurances:
                    occurances[letter] += 1
                else:
                    occurances[letter] = 1

            return occurances

        tally_s = getOccurances(s)
        tally_t = getOccurances(t)

        return tally_s == tally_t