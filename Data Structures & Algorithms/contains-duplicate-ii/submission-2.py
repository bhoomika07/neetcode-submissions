class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for idx, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = [idx]
            else:
                hash_map[num].append(idx)
        for key, value in hash_map.items():
            if len(value) > 1:
                for j in range(len(value)):
                    for m in range(j+1, len(value)):
                        if abs(value[j] - value[m]) <= k:
                            return True
        return False
        