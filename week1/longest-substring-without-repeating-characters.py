class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        container = set()
        max_len = current_len= 0 ; 
        l = 0
        for r in range(s.__len__()):
            while s[r] in container:
                container.remove(s[l]);l += 1
            
            container.add(s[r])
            max_len = max(max_len , r - l + 1)
        return max_len