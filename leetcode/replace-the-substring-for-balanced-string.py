class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        x = len(s) // 4
        grt = {}
        n = len(s)
        for it in count:
            if count[it] > x:
                grt[it] = count[it] - x
        if not grt:
            return 0
        l = 0
        for r in range(len(s)):
            if s[r] in grt:
                grt[s[r]] -= 1 
            while max(grt.values()) <= 0:
                n = min(n, r - l + 1)
                if s[l] in grt:
                    grt[s[l]] += 1
                l += 1
                
        return n