class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                k = j+1
                l = len(nums) - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        k+=1
                        l-=1
                    elif total < target:
                        k+=1
                    elif total > target:
                        l-=1
        return list(ans)

        