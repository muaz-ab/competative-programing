class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx = cur = 0
        for i in range(len(nums)):            
            cur += nums[i]
            if nums[i] > maxx:
                mid = cur / (i + 1)
                val = int(-1 * mid // 1 * -1)
                maxx = max([maxx, val])
        return maxx