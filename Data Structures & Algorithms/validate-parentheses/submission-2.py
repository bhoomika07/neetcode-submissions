class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for char in s:
            if char in char_map.keys():
                if len(stack)!=0 and stack[-1] == char_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return (True)
        else:
            return (False)
        