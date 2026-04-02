class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(n1 + n2)
            elif token == "-":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(n1 - n2)
            elif token == "*":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(n1 * n2)
            elif token == "/":
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(n1 / n2)
            else:
                stack.append(token)

        return int(stack[-1])