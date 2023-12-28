class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = ""
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if int(str(nums[j]) + str(nums[j+1])) < int(str(nums[j+1]) + str(nums[j])):
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
                else:
                    continue
        for nu in nums:
            result += str(nu)
        
        result = result.lstrip('0') or '0'
        return result
                        