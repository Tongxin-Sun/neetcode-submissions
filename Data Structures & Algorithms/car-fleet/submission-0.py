class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()
        
        stack = []
        for i in range(len(cars) - 1, -1, -1):
            if not stack or (target - cars[i][0]) / cars[i][1]  > (target - stack[-1][0]) / stack[-1][1]:
                stack.append(cars[i])
        return len(stack)