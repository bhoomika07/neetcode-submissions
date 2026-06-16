class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                popped = stack.pop()
                res[popped[1]] = idx - popped[1]
            stack.append([temperature, idx])
        return res
        