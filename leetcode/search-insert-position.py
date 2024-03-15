class Solution(object):
    def searchInsert(self, nums, target):
        nums_lower = []
        for i in range(len(nums)):
            if target > nums[i]:
                nums_lower.append(nums[i])
        return len(nums_lower)