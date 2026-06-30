class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        first = strs[0]
        longest_common_prefix = ""

        while i < len(first):
            for string in strs[1:]:
                if i >= len(string) or first[i] != string[i]:
                    return longest_common_prefix
            longest_common_prefix+=first[i]
            i+=1
        return longest_common_prefix


        