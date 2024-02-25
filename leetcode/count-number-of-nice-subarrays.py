class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        count , curcount ,nsub = 0 , 0 ,0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                curcount += 1
                count = 0
            if curcount == k:
                while l < len(nums) and nums[l] % 2 == 0:
                    l += 1
                    count += 1
                count += 1
                curcount -= 1
                l += 1
            nsub += count
        return nsub


        