class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left, right = j+1, len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left+=1
                        right-=1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left+=1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -=1
        return list(ans)
        