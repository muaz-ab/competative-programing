class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0 
        cont = float('inf')
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                cont = min(cont,r-l+1)
                summ -= nums[l]
                l += 1
        return cont if cont != float('inf') else 0 