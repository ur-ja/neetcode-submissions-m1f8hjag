class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, close, path):
            if open < close or open > n:
                return
            if open == n and close == n:
                res.append(path)
                return

            
            backtrack(open + 1, close, path + '(')
            
            backtrack(open, close + 1, path + ')')

        backtrack(0, 0, "")

        return res