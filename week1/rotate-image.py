class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i , j in enumerate(zip(*matrix)):
            matrix[i] = list(j)[::-1]
        