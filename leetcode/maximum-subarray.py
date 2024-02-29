class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0 
        maxx = float('-inf')
        for num in nums:
            if summ < 0:
                summ = 0
            summ += num
            maxx = max(maxx,summ)
        return maxx
