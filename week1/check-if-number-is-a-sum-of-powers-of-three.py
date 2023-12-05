class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        val = 16
        res = 0
        while val >= 0:
            cur_val = 3**val
            if cur_val + res < n:
                res += cur_val
            elif cur_val + res == n:
                return True
            val -= 1
        return False