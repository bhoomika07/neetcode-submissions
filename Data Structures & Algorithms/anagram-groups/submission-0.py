class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        sorted_strs = [sorted(string) for string in strs]
        hash_map = {}
        k = 0
        while k < len(strs):
            if tuple(sorted_strs[k]) not in hash_map.keys():
                hash_map[tuple(sorted_strs[k])] = [strs[k]]
            else:
                hash_map[tuple(sorted_strs[k])].append(strs[k])
            sorted_strs[k].append(strs[k])
            k+=1
        final_ans = []
        for values in hash_map.values():
            final_ans.append(values)
        return (final_ans)



        