class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        start_idx = 0
        
        while start_idx < len(s):
            char_set = set()
            count = 0
            
            # Look ahead from our current starting position
            for i in range(start_idx, len(s)):
                char = s[i]
                
                if char not in char_set:
                    count += 1
                    char_set.add(char)
                    # Update max_count immediately so we don't miss single-char cases
                    max_count = max(count, max_count)
                else:
                    # Hit a duplicate! Stop this run.
                    break
            
            # Move our starting point up by exactly 1 to try the next possibility
            start_idx += 1
            
        return max_count