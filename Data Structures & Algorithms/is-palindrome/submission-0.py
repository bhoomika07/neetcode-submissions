class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_string = ""
        for char in s:
            if char.isalnum():
                s_string+=char

        if s_string == s_string[::-1]:
            return(True)
        return False
        

        