class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res  = []
        container = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i + j) not in container:
                    container[i+j] = [mat[i][j]]
                else:
                    container[i+j] += [mat[i][j]]
        for i , values in container.items():
            if i % 2 != 0:
                res += values
            else:
                res += values[::-1]
        return res