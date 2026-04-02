class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for c in s1:
            count_s1[c] = 1 + count_s1.get(c, 0)

        required = len(count_s1)
        matches = 0
        l = 0

        for r in range(len(s2)):
            if s2[r] in count_s1:
                count_s1[s2[r]] -= 1
                if count_s1[s2[r]] == 0:
                    matches += 1

            while r - l + 1 > len(s1):
                if s2[l] in count_s1:
                    if count_s1[s2[l]] == 0:
                        matches -= 1
                    count_s1[s2[l]] += 1
                l += 1

            if matches == required and r - l + 1 == len(s1):
                return True

        return False