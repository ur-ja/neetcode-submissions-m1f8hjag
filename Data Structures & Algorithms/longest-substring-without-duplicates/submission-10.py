class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        indices = {}

        for r in range(len(s)):
            if s[r] in indices:
                l = max(indices[s[r]] + 1, l)
            indices[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest