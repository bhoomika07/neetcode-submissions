class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        final_ans = []
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num]+=1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in hash_map.items():
            buckets[val].append(key)

        for i in range(len(buckets)-1, 0, -1):
            for bucket in buckets[i]:
                final_ans.append(bucket)
                if len(final_ans) == k:
                    return final_ans
        