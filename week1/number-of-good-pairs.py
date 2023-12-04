class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # l , r = 0 , len(nums)
        counter = 0
        arg = True
        for l in range(len(nums)):
            r = len(nums) - 1
            while l < r:
                if nums[l] == nums[r]:
                    counter += 1
                r -= 1
        return counter
        