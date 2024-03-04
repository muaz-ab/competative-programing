class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            nextrow = [0] * (len(res) + 1)
            for j in range(len(res)):
                nextrow[j] += res[j]
                nextrow[j + 1] += res[j]
            res = nextrow
        return res
