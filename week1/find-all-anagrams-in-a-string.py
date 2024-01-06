from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        qualifier = Counter(p)
        window_size = len(p)
        window = Counter(s[:window_size])
        res = []
        l = 0
        for r in range(len(p) ,len(s)):
            if window == qualifier:
                res.append(l)

            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            
            if len(window) < window_size:
                window[s[r]] += 1
            l += 1
        if window == qualifier:
            res.append(l)
        return  res