class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        final_ans = []
        hash_map = {}
        for string in strs:
            arr = [0]*26
            for char in string:
                arr[ord(char) - ord('a')]+=1
            key = tuple(arr)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(string)

        for values in hash_map.values():
            final_ans.append(values)

        return (final_ans)



        