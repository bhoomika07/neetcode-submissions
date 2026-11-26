class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        substring = set()
        max_len = 0
        while r < len(s):
            while s[r] in substring:
                substring.remove(s[l])
                l+=1
            substring.add(s[r])
            max_len = max(len(substring), max_len)
            r+=1
        return max_len



        