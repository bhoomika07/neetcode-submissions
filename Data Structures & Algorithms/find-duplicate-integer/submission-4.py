class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            i = abs(num) - 1
            if nums[i] < 0:
                return abs(num)
            nums[i]*=-1