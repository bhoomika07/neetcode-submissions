class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        n = len(strs[0])
        k = 0
        first_word = strs[0]
        while k < n:
            for string in strs[1:]:
                if k >= len(string) or first_word[k] != string[k]:
                    return longest_common_prefix
            longest_common_prefix+=first_word[k]
            k+=1
        return longest_common_prefix