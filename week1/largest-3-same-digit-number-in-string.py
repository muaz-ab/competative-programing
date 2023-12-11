class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            temp = ""
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                temp += num[i:i+3]
                if temp >= max_good:
                    max_good = temp
        return max_good