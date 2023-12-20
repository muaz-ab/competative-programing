class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        print(arr)
        idx = 0
        while len(arr) > 1:
            idx = (idx + k -1)%n
            arr.pop(idx)
            n -= 1
        return arr[0]

