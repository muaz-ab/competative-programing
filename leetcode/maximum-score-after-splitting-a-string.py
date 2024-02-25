class Solution:
    def maxScore(self, s: str) -> int:
        summ = 0
        pre = []
        for i in range(len(s)):
            summ += int(s[i])
            pre.append(summ)
        zer = 0
        max_val = 0
        for i in range(len(s)-1):
            if int(s[i]) == 0:
                zer += 1
            else:
                pre[-1] -= 1
            max_val = max(max_val,zer + pre[-1])
        return max_val
        