class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            # Standard bubble sort inner loop
            for j in range(0, len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    # Correctly swap the adjacent elements
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]