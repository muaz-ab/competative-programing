class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cont = {}
        l = 0 
        summ , ans = 0 , 0
        for i , n in enumerate(nums):
            if n in cont:
                while l < cont[n] + 1:
                    summ -= nums[l]
                    l += 1
            summ += n
            ans = max(ans,summ)
            cont[n] = i
        return ans

