class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left, right = 0, n-1
        total = 0
        left_max, right_max = height[0], height[n-1]
        while left < right:
            if left_max < right_max:
                left+=1
                left_max = max(left_max, height[left])
                total+=left_max-height[left]
            else:
                right-=1
                right_max = max(right_max, height[right])
                total+= right_max-height[right]
        return total
