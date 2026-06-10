class Solution:
    def encode(self, strs: list[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> list[str]:
        # 5#hello 5#world
        final_ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            final_ans.append(s[start:end])
            i = end
        return final_ans