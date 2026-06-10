class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1]*len(nums)
        suffix = 1

        for i in range(1,len(nums)):
            prefix_array[i] = prefix_array[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix= suffix*nums[i+1]
            prefix_array[i] = prefix_array[i]*suffix
        return prefix_array
        