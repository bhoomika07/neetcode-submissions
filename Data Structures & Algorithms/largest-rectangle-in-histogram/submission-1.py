class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (idx, h)

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, h*(idx-i))
                start = i
            stack.append((start, height))
        
        for idx, height in stack:
            max_area = max(max_area, height*(len(heights)-idx))
        return max_area
        