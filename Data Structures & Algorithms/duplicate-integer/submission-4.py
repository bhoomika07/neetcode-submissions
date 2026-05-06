class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num]+=1
        for val in hash_map.values():
            if val > 1:
                ans = True
                break
        return ans