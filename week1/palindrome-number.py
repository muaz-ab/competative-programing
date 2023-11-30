class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if str(x) == s[::-1]:
            return True
        else:
            return False