class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += f"{length}#{word}" 

        return encoded


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0


        while i < len(s):
            matched = re.match('([0-9]+)#', s[i:])
            if matched:
                word_length = int(matched.group(1))
                word_start = i + len(matched.group(0))
                word = s[word_start : word_start + word_length]
                res.append(word)
                i = word_start + word_length
            else:
                break

        return res