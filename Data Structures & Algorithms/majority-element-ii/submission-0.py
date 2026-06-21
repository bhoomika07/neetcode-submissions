class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = {}
        n = len(nums)
        ans = []
        for num in nums:
            if num not in hash_map:
                hash_map[num] =1
            else:
                hash_map[num]+=1
        for key, value in hash_map.items():
            if value > n/3:
                ans.append(key)
        return ans

        