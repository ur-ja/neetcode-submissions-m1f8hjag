class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        num_fleets = 0
        stack = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort()
        
        for i in range(len(cars) - 1, -1, -1):
            pos, sp = cars[i]
            t = (target - pos) / sp
            stack.append(t)
            if stack and len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)