class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        
        # Zip pairs characters up to the length of the shorter string
        for char1, char2 in zip(word1, word2):
            ans.append(char1)
            ans.append(char2)
        
        # Slice and append whatever is left over from the longer string
        min_len = min(len(word1), len(word2))
        ans.append(word1[min_len:])
        ans.append(word2[min_len:])
        
        return "".join(ans)