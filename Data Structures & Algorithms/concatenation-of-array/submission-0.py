class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*2*n
        for idx,num in enumerate(nums):
            ans[idx] = num
        
        for idx,num in enumerate(nums):
            ans[n+idx] = num
        return ans
        
        