class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0]*(len(s)+1)
        for i , j , k in shifts:
            shift[i] += 1 if k == 1 else -1
            shift[j+1] -= 1 if k == 1 else -1

        res = []
        for i in range(len(s)):
            if i : shift[i] += shift[i-1]
            res.append(chr((ord(s[i]) - ord("a") + shift[i]) % 26 + ord("a")))
        return "".join(res)