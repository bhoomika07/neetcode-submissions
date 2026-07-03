class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            char_map = [0]*26
            for char in string:
                if char_map[ord(char.upper())-65] != 0:
                    char_map[ord(char.upper())-65]+=1
                else:
                    char_map[ord(char.upper())-65] = 1
            if (tuple(char_map)) in hash_map:
                hash_map[tuple(char_map)].append(string)
            else:
                hash_map[tuple(char_map)] = [string]
        final_ans = []
        for values in hash_map.values():
            final_ans.append(values)
        return final_ans
            
        