class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxn = 0
        leng = 0
        for i in range(len(flips)):
            curr = flips[i]
            maxn = max(maxn , curr)
            if (i + 1) ==  maxn:
                leng += 1
            else:
                continue
        return leng