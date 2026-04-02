class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        count = {}

        for letter in s1:
            count[letter] = 1 + count.get(letter, 0)

        matches = 0
        needed = len(count)

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

            if matches == needed:
                return True

        return False