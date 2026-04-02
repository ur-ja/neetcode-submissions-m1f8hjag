class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        count = [0] * 26
        needed = 0
        matches = 0

        for c in s1:
            idx = ord(c) - ord('a')
            if count[idx] == 0:
                needed += 1
            count[idx] += 1

        for r in range(len(s2)):
            ir = ord(s2[r]) - ord('a')
            count[ir] -= 1
            if count[ir] == 0:
                matches += 1
            elif count[ir] == -1:
                matches -= 1


            if r - l + 1 > len(s1):
                il = ord(s2[l]) - ord('a') 
                count[il] += 1
                if count[il] == 0:
                    matches += 1
                elif count[il] == 1:
                    matches -= 1
                l += 1

            if matches == needed:
                return True

        return False