class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] == nums[j]) and ((i * j)%k == 0) and (0 <= i < j < len(nums)):
                    count += 1
        return count