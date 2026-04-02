class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = {}

        for c in s1:
            count[c] = 1 + count.get(c, 0)

        matches = 0
        required = len(count)
        l = 0

        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1
                if count[s2[r]] == 0:
                    matches += 1
            
            if r - l + 1 > len(s1):
                if s2[l] in count:
                    if count[s2[l]] == 0:
                        matches -= 1
                    count[s2[l]] += 1
                l += 1

            if matches == required:
                return True

        return False

