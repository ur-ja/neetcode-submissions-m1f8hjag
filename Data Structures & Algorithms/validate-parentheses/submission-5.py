class Solution:
    def isValid(self, s: str) -> bool:
        # brackets = {
        #     '(' : ')',
        #     '[' : ']',
        #     '{' : '}'
        # }
        if len(s) % 2 != 0:
            return False


        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []

        for b in s:
            if b not in brackets:
                stack.append(b)
            else :
                if not stack:
                    return False
                val = stack.pop()
                if val != brackets[b]:
                    return False

        if len(stack) > 0:
            return False
        return True