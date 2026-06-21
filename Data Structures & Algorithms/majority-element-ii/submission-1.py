class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = num2 = -1
        count1 = count2 = 0
        n = len(nums)
        for num in nums:
            if num == num1:
                count1+=1
            elif num == num2:
                count2+=1
            elif count1 == 0:
                count1 = 1
                num1 = num
            elif count2 == 0:
                count2 = 1
                num2 = num
            else:
                count1-=1
                count2-=1
        
        count1 = count2 = 0
        for num in nums:
            if num == num1:
                count1+=1
            elif num == num2:
                count2+=1
        
        res = []
        if count1 > n//3:
            res.append(num1)
        if count2 > n//3:
            res.append(num2)
        return res

        