class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for i in range(len(trips)):
            if trips[i][2] > n:
                n = trips[i][2]
        mat = [0]*n
        for i in range(len(trips)):
            mat[trips[i][1]] += trips[i][0]
            if trips[i][2] < len(mat):
                mat[trips[i][2]] -= trips[i][0]
        pre = []
        summ = 0
        for i in range(len(mat)):
            summ += mat[i]
            pre.append(summ)
        if max(pre) > capacity:
            return False
        else:
            return True