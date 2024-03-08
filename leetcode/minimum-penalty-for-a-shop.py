class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        s = [0] * (n + 1)
        for i, chx in enumerate(customers):
            s[i + 1] = s[i] + int(chx == 'Y')
        res, curr = 0, inf
        for j in range(n + 1):
            t = j - s[j] + s[-1] - s[j]
            if curr > t:
                res, curr = j, t
        return res
