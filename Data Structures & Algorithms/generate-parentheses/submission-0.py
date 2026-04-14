class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(path, open, close):
            # needs to stop when num "(" and ")" = n 
            if close > open:
                return
            if open == n and close == n:
                res.append(path)
                return
            if open > n or close > n:
                return
            
            backtrack(path + "(", open + 1, close)
        
            backtrack(path + ")", open, close + 1)
        
        backtrack("", 0, 0)
        
        return res
        