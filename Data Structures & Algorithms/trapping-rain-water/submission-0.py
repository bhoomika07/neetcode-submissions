class Solution:
    def trap(self, height: List[int]) -> int:
        total_water_stored = 0
        for i in range(len(height)):
            # water[i] = min(max_left, max_right) - height[i]
            max_left = max(height[0:i]) if i > 0 else 0
            max_right = max(height[i+1:]) if i < len(height) - 1 else 0
            water_block = min(max_left, max_right) - height[i]
            if water_block > 0:
                total_water_stored+=water_block
        return total_water_stored
        