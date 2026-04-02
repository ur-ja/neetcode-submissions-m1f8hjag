class Solution:
    # Binary shift w ascii or something

    def encode(self, strs: List[str]) -> str:
        # "number#string"
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        #    5#Hello5#World
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            decoded.append(word)
            i = end

            
        return decoded