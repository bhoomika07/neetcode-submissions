class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        curr_streak = 1
        longest_streak = 1

        for num in nums:
            if num-1 not in num_set:
                curr_streak = 1
                while num+1 in num_set:
                    curr_streak+=1
                    num = num+1
                longest_streak = max(longest_streak, curr_streak)

        return (longest_streak)


        