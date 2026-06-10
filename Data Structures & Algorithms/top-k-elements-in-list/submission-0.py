class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num]+=1

        sorted_map = list(hash_map.items())

        sorted_map.sort(key=lambda x: x[1], reverse=True)

        final_ans = []
        while k:
            final_ans.append(sorted_map[k-1][0])
            k-=1
        return (final_ans)
                
        