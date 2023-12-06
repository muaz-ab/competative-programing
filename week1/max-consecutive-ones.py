class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current = 0
            if nums[i] == 1:
                current += 1
                max_len = max(max_len , current)
                
        return max_len