class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:
            while (s[l] == " " or (not s[l].isalnum())) and l < r:
                l += 1
            while (s[r] == " " or (not s[r].isalnum())) and l < r:
                r -= 1
            if s[r] != s[l]:
                return False
            l += 1
            r -= 1

        return True