class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastgood = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= lastgood:
                lastgood = i
        return lastgood == 0
