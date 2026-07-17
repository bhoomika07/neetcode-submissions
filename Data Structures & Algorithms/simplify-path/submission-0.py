class Solution:
    def simplifyPath(self, path: str) -> str:
        unix_chars = path.split('/')
        final_ans_stack = []
        print(unix_chars)
        for unix_char in unix_chars:
            if unix_char == "..":
                if final_ans_stack:
                    final_ans_stack.pop()
            elif unix_char in (".", "", " "):
                continue
            else:
                final_ans_stack.append(unix_char)
        return "/"+"/".join(final_ans_stack)

        