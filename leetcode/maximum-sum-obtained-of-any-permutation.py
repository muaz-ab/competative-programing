class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        f = [0] * (len(nums) + 1)
        for start , end in requests:
            f[start] += 1
            f[end + 1] -= 1
        for i in range(1 , len(f)):
            f[i] += f[i - 1]
        res , modulo = 0 , (10 ** 9) + 7
        nums.sort(reverse = True)
        f.sort(reverse = True)
        for n , count in zip(nums , f):
            res += count * n
        return res % modulo