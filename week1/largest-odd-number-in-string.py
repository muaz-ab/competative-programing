class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        for i in range(len(num) - 1, -1, -1):
            if eval(num[i]) % 2 == 1:
                return num[:i+1]
        
        return ""