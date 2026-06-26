class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums_copy = [0]*n
        for idx,num in enumerate(nums):
            nums_copy[(idx+k)%n] = nums[idx]
        nums[:] = nums_copy
        