class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, colder_day = stack.pop()
                res[colder_day] = day - colder_day
            stack.append((temp, day))
            
        return res