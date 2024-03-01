class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == 0:
                    continue 
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += max(0, k - j - 1)
        return count