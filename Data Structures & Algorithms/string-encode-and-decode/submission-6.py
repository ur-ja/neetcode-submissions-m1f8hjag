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

        # Main loop to process the encoded string
        while i < len(s):
            # Use regex to find the length (digits before '#') and the position of the '#'
            match = re.match(r'(\d+)#', s[i:])
            if match:
                length = int(match.group(1))  # Extract the length
                j = i + len(match.group(0))  # Update the pointer to the start of the actual string
                res.append(s[j:j + length])  # Extract the string based on the length
                i = j + length  # Move the pointer to the next encoded segment
            else:
                break  # No valid match, break the loop
        
        return res