class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        ans = []
        zero_idx = 0
        for idx,num in enumerate(nums):
            if num == 0:
                zero_idx = idx
                zero_count+=1

        if zero_count == 0:
            product = 1
            for num in nums:
                product*=num
            for num in nums:
                ans.append(product//num)
        elif zero_count > 1:
            ans = [0]*len(nums)
        else:
            product = 1
            for idx, num in enumerate(nums):
                if idx!=zero_idx:
                    product = product* num
            for idx,num in enumerate(nums):
                if idx == zero_idx:
                    ans.append(product)
                else:
                    ans.append(0)
        return ans