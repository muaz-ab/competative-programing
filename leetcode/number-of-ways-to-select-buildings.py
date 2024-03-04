class Solution:
    def numberOfWays(self, s: str) -> int:
        count = Counter(s)
        i, j = 0 , 0
        result = 0
        for itm in s:
            if itm == "1":
                result += i * (count["0"] - i)
                j  += 1
            else:
                result += j * (count["1"] - j)
                i += 1
        return result