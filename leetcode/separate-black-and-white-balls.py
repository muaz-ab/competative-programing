class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        summ = 0
        for i in range(len(s)-1,-1,-1):
            print(s[i])
            if s[i] == '0':
                count += 1
            elif s[i] == '1':
                summ += count
        return summ