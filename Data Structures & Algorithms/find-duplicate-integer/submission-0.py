class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = {}
        for num in nums:
            if num not in hash_set:
                hash_set[num] = 1
            else:
                hash_set[num]+=1
        
        for key,value in hash_set.items():
            if value > 1:
                return int(key)
        