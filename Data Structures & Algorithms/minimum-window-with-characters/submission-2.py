class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        countT, countW = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l, have = 0, 0
        needed = len(countT)
        shortestSubstring = ""

        for r in range(len(s)):
            countW[s[r]] = 1 + countW.get(s[r], 0)
            if s[r] in countT and countW[s[r]] == countT[s[r]]:
                have += 1

            while have == needed:
                if shortestSubstring == "" or r - l + 1 < len(shortestSubstring):
                    shortestSubstring = s[l:r+1]

                countW[s[l]] -= 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return shortestSubstring

        