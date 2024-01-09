class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        res_cu = 0
        l = 0
        count = Counter()
        if len(nums) == sum(num for num in nums):
            return len(nums) - 1
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[0] > 1:
                count[nums[l]] -= 1
                l += 1
            res_cu = count[1]
            res = max(res , res_cu)
        return res