class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 1
        seen = set()
        seen.add(s[l])
        length = 1
        longest = 0
        while r < len(s):
            if s[r] in seen:
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    length -= 1
                    l += 1
            seen.add(s[r])
            length += 1
            longest = max(length, longest)
            r += 1

        return longest