class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        count = {}

        for c in t:
            count[c] = 1 + count.get(c, 0)

        l, matches = 0, 0
        needed = len(count)
        shortestSubstring = ""

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    matches += 1 

            while matches == needed:
                if shortestSubstring == "" or r - l + 1 < len(shortestSubstring):
                    shortestSubstring = s[l: r + 1]

                if s[l] in count:
                    if count[s[l]] == 0:
                        matches -= 1
                    count[s[l]] += 1
                l += 1

        return shortestSubstring

        