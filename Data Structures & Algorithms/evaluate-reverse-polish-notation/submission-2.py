class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "-":
                stack.append(int(stack.pop()) - int(stack.pop()))
            elif token == "*":
                stack.append(int(stack.pop()) / int(stack.pop()))
            else:
                stack.append(token)
            
        return stack[0]