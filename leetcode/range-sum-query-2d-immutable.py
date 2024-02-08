class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row , col = len(matrix) , len(matrix[0])
        self.prefixsum = [[0] * (col + 1) for _ in range(row + 1)]
        for r in range(row):
            summ = 0
            for c in range(col):
                summ += matrix[r][c]
                above = self.prefixsum[r][c+1]
                self.prefixsum[r+1][c+1] = summ + above
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.prefixsum[row2][col2] - self.prefixsum[row2][col1 - 1] - self.prefixsum[row1 - 1][col2 ] + self.prefixsum[row1 - 1][col1 - 1]
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)