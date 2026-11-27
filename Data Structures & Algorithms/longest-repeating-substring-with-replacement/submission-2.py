class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_len = 0
        hash_map = {}
        for right in range(len(s)):
            if s[right] not in hash_map:
                hash_map[s[right]] = 1
            else:
                hash_map[s[right]]+=1
            
            replacements = (right-left+1) - max(hash_map.values())
            while replacements > k:
                hash_map[s[left]]-=1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                replacements-=1
                left+=1
            max_len = max(max_len, right-left+1)

        return max_len
        