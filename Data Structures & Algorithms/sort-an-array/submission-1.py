class Solution:
    def merge(self,left_array, right_array):
        l = 0
        r = 0
        res = []
        while l < len(left_array) and r < len(right_array):
            if left_array[l] <= right_array[r]:
                res.append(left_array[l])
                l+=1
            else:
                res.append(right_array[r])
                r+=1
        while l < len(left_array):
            res.append(left_array[l])
            l+=1
        while r < len(right_array):
            res.append(right_array[r])
            r+=1
        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_array = self.sortArray(nums[0:mid])
        right_array = self.sortArray(nums[mid:])
        final_ans = self.merge(left_array,right_array)
        return final_ans

        
        
        