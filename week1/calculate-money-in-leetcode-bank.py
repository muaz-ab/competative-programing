class Solution:
    def totalMoney(self, n: int) -> int:
        q = n // 7
        r = n % 7
        full_week = q*28 + 7*q*(q-1)//2
        rem_days = r*(r+1)//2 + r*q
        return full_week + rem_days