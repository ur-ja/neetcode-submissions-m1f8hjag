class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        return sorted(s) == sorted(t)
        """
        Given: string s and string t
        return: True if s and t are anagrams
                False otherwise

        anagram: exact same characters

        sets not poss because number of occurances will not be counted

        dictionary makes sense we can keep a tally of how many times each letter has occurred
        then compare
    
        Time complexity = O(n + n) = O(2n) = O(n) 

        Space complexity = O(n + n)  = O(2n) = O(n) -> solution takes too much space

        we can try sorting both and then comparing

        storage is still O(n) cause we are storing 2 input strings


        """

