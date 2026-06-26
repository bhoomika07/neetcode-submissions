class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        k = k%len(nums)
        def reverse_arr(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        reverse_arr(l,r)
        reverse_arr(l,k-1)
        reverse_arr(k,r)
        