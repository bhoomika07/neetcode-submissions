class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        for char in s:
            if not char.isalnum():
                s = s.replace(char,"")

        right = len(s) - 1
        left = 0

        mid = len(s)//2

        if mid%2!=0:
            for i in range(0,mid):
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        else:
            for i in range(0,mid):
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True