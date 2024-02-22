class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ["a" , "e" , "i" , "o" ,"u"]
        l = 0 
        window = []
        res = []
        count = 0
        for r in range(len(s)):
            window.append(s[r])
            if s[r] in vowel:
                count += 1
            if len(window) == k:
                res.append(count)
                if s[l] in vowel:
                    count -= 1
                window.remove(s[l])
                l += 1
            while len(window) > k:
                if s[l] in vowel:
                    count -= 1
                window.remove(s[l])
                l += 1
        return max(res) if res else 0

            