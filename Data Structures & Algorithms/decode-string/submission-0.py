class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substring = []
                while stack and stack[-1]!= '[':
                    popped = stack.pop()
                    substring.append(popped)
                stack.pop()
                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                count = int("".join(reversed(k)))
                string_segment = "".join(reversed(substring))

                stack.append(string_segment * count)

        return "".join(stack)
        