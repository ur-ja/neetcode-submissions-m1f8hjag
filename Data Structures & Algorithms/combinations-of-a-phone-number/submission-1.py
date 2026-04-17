class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        # digits = "34"
        def dfs(i, path):
            if len(path) == len(digits):
                res.append(path)
                return
            for j in mapping[digits[i]]:
                dfs(i + 1, path + j)

        dfs(0, "")
        return res

            