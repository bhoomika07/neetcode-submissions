class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        max_left = [0]* len(height)
        max_right = [0]* len(height)
        
        max_left[0] = height[0]
        max_right[len(height)-1] = height[len(height) - 1]
        
        total = 0 

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])
        for j in range(len(height)-2,-1, -1):
            max_right[j] = max(max_right[j+1], height[j])
        
        for i in range(len(height)):
            water_block = min(max_left[i], max_right[i]) - height[i]
            if water_block > 0:
                total+=water_block
        return total




        