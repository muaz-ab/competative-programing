class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort(reverse=True)
        res = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                res += i+1
        return res                