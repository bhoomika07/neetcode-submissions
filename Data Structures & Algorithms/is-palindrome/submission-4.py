class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_copy = ""
        for char in s:
            if char.isalnum():
                s_copy+=char
        l = 0
        r = len(s_copy) - 1
        while l < r:
            if s_copy[l] != s_copy[r]:
                return False

            l+=1
            r-=1
        return True
        