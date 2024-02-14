class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = 0
        nums.sort()
        for i in range(len(nums)-2):
            window = nums[i:i+3]
            if (sum(window) - max(window)) > (max(window)):
                current_sum = sum(window)
                max_sum = max(max_sum , current_sum)
        return max_sum