class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        count = 0
        
        while i < n:
            for j in range(i+1,n):
                if  (nums[i] + nums[j]) < target:
                    count += 1
            i += 1
        return count