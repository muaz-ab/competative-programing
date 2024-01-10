from collections import Counter
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        l = 0
        count = Counter()
        for r in range(len(answerKey)):
            count[answerKey[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[answerKey[l]] -= 1
                l += 1
            res = max(res , r - l + 1)
        return res
            