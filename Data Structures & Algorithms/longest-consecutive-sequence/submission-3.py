class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))
        longest_streak = 1
        current_streak = 1

        for idx,num in enumerate(nums):
            if idx+1 < len(nums):
                if nums[idx+1] == num+1:
                    current_streak+=1
                else:
                    longest_streak = max(current_streak, longest_streak)
                    current_streak = 1
        return max(longest_streak, current_streak)