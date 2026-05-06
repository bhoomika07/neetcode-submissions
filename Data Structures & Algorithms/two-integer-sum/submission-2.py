class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hash_map = {}
        for idx, num in enumerate(nums):
            if target - num in hash_map:
                j = hash_map[target-num]
                ans.append(j)
                ans.append(idx)
                return ans
            hash_map[num] = idx