class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        char_set = set()
        for r in range(l,len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(r-l+1, max_len)
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l+=1
            char_set.add(s[r])
            max_len = max(r - l + 1, max_len)
        return max_len


        