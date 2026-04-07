class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 + n1)
            elif token == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 * n1)
            elif token == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif token == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(token))
            
        return int(stack[-1])