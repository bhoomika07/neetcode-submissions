class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        max_value = 0
        majority_element = nums[0]
        for num in nums:
            if num not in hash_map:
                hash_map[num]=1
            hash_map[num] +=1
        for key, value in hash_map.items():
            if hash_map[key] > max_value:
                max_value = hash_map[key]
                majority_element = key
        return majority_element

        