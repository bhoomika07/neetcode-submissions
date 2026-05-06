class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        nums = sorted(nums)
        for idx, num in enumerate(nums):
            j = idx+1
            if j < len(nums):
                if num == nums[j]:
                    ans = True
                    break
        return ans
        