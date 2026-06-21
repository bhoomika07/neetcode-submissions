class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # [1,3] target = 2
        # l = 0, r = 1, mid = 0= nums[0] = 1, 1< 2
        # l = mid+1 = 1 l = 1, r = 1, mid = 1, 3>2
        # now l = 1 r = 0

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
        return l
        
