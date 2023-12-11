class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                code = int(s[i:i+2])
                result += chr(96 + code)
                i += 3
            else:
                code = int(s[i])
                result += chr(96 + code)
                i += 1
        return result