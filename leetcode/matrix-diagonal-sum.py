class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j or i + j == len(mat[i]) - 1:
                    total_sum += mat[i][j]

        return total_sum