class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        mat = [0]*n
        for j in range(len(bookings)):
            r = bookings[j][1] -1
            l = bookings[j][0] -1
            k = bookings[j][2]
            mat[l] += k
            if r < len(mat)-1:
                mat[r+1] -= k
        pre = []
        summ = 0
        for i in range(len(mat)):
            summ += mat[i]
            pre.append(summ)
        return pre
            