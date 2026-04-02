class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if stack:
                val, idx = stack[-1]
                while stack and temp > val:
                    res[idx] = i - idx
                    stack.pop()
                    if stack:
                        val, idx = stack[-1]
            
            stack.append((temp, i))
                
        return res