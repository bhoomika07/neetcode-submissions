class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for idx, num in enumerate(nums):
            if num not in seen:
                seen[num] = [idx]
            else:
                seen[num].append(idx)
        print(seen)
        for value in seen.values():
            if len(value) > 1:
                left = 0
                right = left+1
                while right < len(value):
                    if abs(value[left]-value[right]) <=k:
                        return True
                    elif abs(value[left]-value[right]) > k:
                        left+=1
                    right+=1
        return False 

        