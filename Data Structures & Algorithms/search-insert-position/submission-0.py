class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx,num in enumerate(nums):
            if num == target:
                return idx
            if num > target:
                return idx
        if idx == len(nums)-1:
            return idx+1