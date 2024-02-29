class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                res += 1
                maxDoubles -= 1
                continue
            if maxDoubles == 0:
                res += target - 1
                break
            else:
                target -= 1
                res += 1
        return res
